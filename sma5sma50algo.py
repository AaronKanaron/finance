import yfinance as yf
import pandas as pd

ticker = yf.Ticker("INVE-A.ST")

hist = ticker.history(period="1y", interval="1h", repair=True)

def calculate_smax(df, x):
    return df['Close'].rolling(window=x).mean()

def calculate_growth_rate(df, days=3):
    return (df['Close'] - df['Close'].shift(days)) / df['Close'].shift(days) * 100

hist = hist.sort_index()

hist['SMA50'] = calculate_smax(hist, 50)
hist["SMA5"] = calculate_smax(hist, 5)
hist['Growth_Rate_3D'] = calculate_growth_rate(hist, 3)

# hist["Datetime"] = pd.to_datetime(hist["Datetime"])

def check_sma_exceeds(df):
    df_filtered = df.dropna(subset=['SMA5', 'SMA50'])
    crosses = (df_filtered['SMA5'] > df_filtered['SMA50']) & (df_filtered['SMA5'].shift(1) <= df_filtered['SMA50'].shift(1))
    result = df_filtered[crosses][['Growth_Rate_3D']]
    result = result.reset_index()['Growth_Rate_3D']
    if result > 1: return
    return result

print(check_sma_exceeds(hist))

# print(hist[['SMA5', 'SMA50', "Growth_Rate_3D"]])

# hist.to_csv("sma50.csv")


# 205.06, 204.23
# 205.10, 204.81
# 205.15, 205.30  | KÖP
# 205.22, 206.02
# 205.30, 206.80