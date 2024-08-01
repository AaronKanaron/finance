import yfinance as yf # type: ignore
import os
import json
import numpy as np # type: ignore
from sklearn.preprocessing import StandardScaler  # type: ignore
from sklearn.ensemble import RandomForestRegressor # type: ignore


def calculate_growth(values):
    if len(values) < 2 or values[-1] == 0:
        return 0
    else:
        try:
            growth_rate = (values[0] / values[-1]) ** (1 / (len(values) - 1)) - 1
            if isinstance(growth_rate, complex):
                return 0
            return growth_rate
        except ZeroDivisionError:
            return 0

def get_financial_data(income_stmt, field):
    try:
        data = income_stmt.loc[field].dropna().values.tolist()
        return data if data else [0]  # Return [0] if the list is empty
    except KeyError:
        # If the field doesn't exist in the income statement
        return [0]
    except Exception as e:
        print(f"Error retrieving {field}: {str(e)}")
        return [0]

def collect_metrics(symbol):
    ticker = yf.Ticker(symbol)

    info = ticker.info
    balance_sheet = ticker.balance_sheet
    income_stmt = ticker.income_stmt

    # Revenue Growth
    revenue = get_financial_data(income_stmt, "Operating Revenue")
    revenue_growth = calculate_growth(revenue)

    # Earning Growth
    earnings = get_financial_data(income_stmt, "EBIT")
    if earnings == 0: earnings = get_financial_data(income_stmt, "Net Income")
    earnings_growth = calculate_growth(earnings)
    if earnings_growth == 0: return

    ttm_net_income_arr = get_financial_data(ticker.quarterly_income_stmt, "Net Income")
    ttm_net_income = sum(ttm_net_income_arr[:4])
    # print(ttm_net_income)
    #ROIC
    net_income = get_financial_data(income_stmt, "Net Income")[0]
    total_debt = get_financial_data(balance_sheet, "Total Debt")[0]
    cash = get_financial_data(balance_sheet, "Cash And Cash Equivalents")[0]
    equity = sum(get_financial_data(balance_sheet, "Common Stock Equity"))
    roic = sum(get_financial_data(income_stmt, "Net Income")) / (
        sum(get_financial_data(balance_sheet, "Total Debt"))+equity-sum(get_financial_data(balance_sheet, "Cash And Cash Equivalents"))
        )
    stockholder_equity = get_financial_data(balance_sheet, "Stockholders Equity")[0]
    goodwill = get_financial_data(balance_sheet, "Goodwill")[0]

    operating_income = sum(get_financial_data(income_stmt, "Operating Income"))
    interest_expenses = get_financial_data(income_stmt, "Interest Expense")[0]
    tax_rate = get_financial_data(income_stmt, "Tax Rate For Calcs")[0]
    non_operating_income = get_financial_data(income_stmt, "Interest Income Non Operating")[0]
    after_tax_operating_income = net_income + interest_expenses * (1 - tax_rate) - non_operating_income * (1 - tax_rate)
    invested_capital = total_debt + stockholder_equity - cash - goodwill
    invested_capital_yf = get_financial_data(balance_sheet, "Invested Capital")[0]
    pretax = get_financial_data(income_stmt, "Pretax Income")[0]
    tax_expenses = pretax * tax_rate
    ebit = get_financial_data(income_stmt, "EBIT")[0]
    ebit_calc = net_income + interest_expenses + tax_expenses

    terminal_width = os.get_terminal_size().columns

    variables = [
        ('net_income', net_income),
        ('total_debt', total_debt),
        ('cash', cash),
        ('equity', equity),
        ('stockholder_equity', stockholder_equity),
        ('goodwill', goodwill),
        ('operating_income', operating_income),
        ('interest_expenses', interest_expenses),
        ('tax_rate', tax_rate),
        ('non_operating_income', non_operating_income),
        ('after_tax_operating_income', after_tax_operating_income),
        ('invested_capital', invested_capital),
        ('invested_capital_yf', invested_capital_yf),
        ('ebit', ebit),
        ("ebit_calc", ebit_calc),
        ("pretax", pretax),
        ("tax_expenses", tax_expenses)
    ]

    # print("\n" + "=" * terminal_width)
    # print("Financial Variables Debug Output".center(terminal_width))
    # print("=" * terminal_width)

    # for name, value in variables:
    #     print(f"| {name:<28} | {value:>45} |")
    #     print("-" * terminal_width)

    # print("=" * terminal_width + "\n")



    # print(f"After tax operating income: {after_tax_operating_income}, invested capital: {invested_capital}")
    # print(f"ROIC: {after_tax_operating_income*(1-tax_rate)/invested_capital*100:2f}%")
    # print(f"ROIC other: {operating_income*(1 - tax_rate) / invested_capital*100:2f}%      | Absolut fel")
    # print(f"ROIC Alvin: {roic*100:2f}%")
    # print(f"ROIC #4: {ebit*(1-tax_rate)/invested_capital_yf*100:2f}%")
    # print(f"ROIC #5 (scuff): {ebit_calc*(1-tax_rate)/invested_capital_yf*100:2f}%")


    #P/E
    
    if "marketCap" in info and ttm_net_income != 0:
        trailingPE = info["marketCap"] / ttm_net_income
    elif "marketCap" in info:
        trailingPE = info["marketCap"]
    else:
        trailingPE = None  # or any default value you prefer
    # yfPE = info["trailingPE"]

    # expected_PE = model.predict(normalized_features)[0]

    # Compare actual trailingPE with expected PE
    # performance_ratio = yfPE / expected_PE

    # print(f"Actual trailing PE: {yfPE:.2f}")
    # print(f"Expected PE based on financials: {expected_PE:.2f}")
    # print(f"Performance ratio: {performance_ratio:.2f}")

    data = {    
        "ticker": symbol,
        "currency": info.get("financialCurrency", "--"),
        "industry": info.get("industryKey", "--"),
        "metrics": {
            "p_e": trailingPE,
            "own_p_e": trailingPE,
            "current_price": info.get('currentPrice', "--"),
            "revenue_growth": revenue_growth,
            "earnings_growth": earnings_growth,
            # "ebitda": EBITDA,
        }
    }


    return data

def main():
    with open("output.json", "r") as ticker_data:
        tickers = json.load(ticker_data)

    data = []
    for idx, ticker in enumerate(tickers):
        if idx >= 20: 
            break
        print(f"{ticker["symbol"]} – {idx}/6400")
        collected_data = collect_metrics(ticker["symbol"])
        # print("BETSON")
        # collected_data = collect_metrics("TSLA")
        data.append(collected_data)
        # print(ticker["symbol"])

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

main()