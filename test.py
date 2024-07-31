import yfinance as yf

ticker = yf.Ticker("AAPL")

shares = ticker.get_shares_full(start="2024-01-01", end=None)
shares.to_csv("shares.csv")
print(shares.iloc[-1])