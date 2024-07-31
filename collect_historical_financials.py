import yfinance as yf # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor

ticker = yf.Ticker("AAPL")
net_income = 96995000

df = ticker.history(period="6mo", interval="1h", actions=True)
df.to_csv("ticker_history.csv")

shares = ticker.get_shares_full(start="2024-01-01", end=None)
shares_outstanding = shares.iloc[-1]

eps = net_income / shares_outstanding

df['PE'] = df['Close'] / eps

# def calculate_pe(row, net_income):
#     return row['Close'] / (net_income / len(df)) if net_income != 0 else np.nan

# df['PE'] = df.apply(lambda row: calculate_pe(row, net_income), axis=1)

# Print PE statistics
print("PE Statistics:")
print(df['PE'].describe())
print("\nNumber of zero PE values:", (df['PE'] == 0).sum())
print("Number of NaN PE values:", df['PE'].isna().sum())

# Check the last few PE values
print("\nLast 5 PE values:")
print(df['PE'].tail())

# Check the components of PE calculation
print("\nLast 5 Close prices:")
print(df['Close'].tail())
print("\nNet Income:", net_income)
print("\nShares Outstanding:", shares_outstanding)


# Feature engineering
df['Log_Returns'] = np.log(df['Close'] / df['Close'].shift(1))
df['Log_Volume_Change'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['Price_Range'] = (df['High'] - df['Low']) / df['Open']
df['MA_50'] = df['Close'].rolling(window=50).mean()
df['MA_200'] = df['Close'].rolling(window=200).mean()

# Update features list
features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Log_Returns', 'Log_Volume_Change', 'Price_Range', 'MA_50', 'MA_200']
X = df[features]
y = df['PE']

# Check for infinities and NaNs
inf_columns = X.columns[X.isin([np.inf, -np.inf]).any()].tolist()
nan_columns = X.columns[X.isna().any()].tolist()

if inf_columns:
    print("Columns with infinity:")
    for col in inf_columns:
        print(f"{col}: {X[col].isin([np.inf, -np.inf]).sum()} infinite values")

if nan_columns:
    print("Columns with NaN:")
    for col in nan_columns:
        print(f"{col}: {X[col].isna().sum()} NaN values")

# Replace infinite values with NaN and then drop rows with NaN
X = df[features].dropna()
y = df['PE'].loc[X.index]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = RobustScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

# Train model
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
# Perform cross-validation
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print("\nCross-validation scores:", cv_scores)
print("Mean CV score:", cv_scores.mean())

# Fit model
model.fit(X_train_scaled, y_train)
# Predict
current_financials = X.iloc[-1:] 
current_financials_scaled = pd.DataFrame(scaler.transform(current_financials), columns=current_financials.columns, index=current_financials.index)
expected_PE = model.predict(current_financials_scaled)[0]

actual_PE = y.iloc[-1]

print(f"\nActual trailing PE: {actual_PE:.2f}")
print(f"Expected PE based on model: {expected_PE:.2f}")

if actual_PE > 0 and expected_PE > 0:
    performance_ratio = actual_PE / expected_PE
    print(f"Performance ratio: {performance_ratio:.2f}")

    if performance_ratio > 1:
        print("The stock is trading above expected levels based on its financials.")
    elif performance_ratio < 1:
        print("The stock is trading below expected levels based on its financials.")
    else:
        print("The stock is trading at expected levels based on its financials.")
else:
    print("Unable to calculate performance ratio due to zero or negative PE values.")

# Print feature importances
importances = pd.DataFrame({'feature': features, 'importance': model.feature_importances_})
print("\nFeature Importances:")
print(importances.sort_values('importance', ascending=False))
