import pandas as pd

df = pd.read_excel("Consolidated_Stock_Data1.xlsx")

df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values(by=["Company Name", "Date"])

df["20-Day MA"] = df.groupby("Company Name")["Close"].transform(lambda x: x.rolling(window=20, min_periods=1).mean())

df["Daily Return"] = df.groupby("Company Name")["Close"].transform(lambda x: x.pct_change())

df["Daily Return"] = df["Daily Return"].fillna(0)

df.to_excel("Updated_Stock_Data_with_20Day_MA.xlsx", index=False)

print("20-day moving average and daily returns calculated. Updated file saved as 'Updated_Stock_Data_with_20Day_MA_and_Daily_Return.xlsx'.")
