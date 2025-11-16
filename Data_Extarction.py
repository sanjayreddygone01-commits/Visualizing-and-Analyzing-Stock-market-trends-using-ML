import yfinance as yf
import pandas as pd

def stocks_data(tickers, company_names, start_date, end_date, output_file):
    

    with pd.ExcelWriter(output_file) as writer:
        for ticker, company_name in zip(tickers, company_names):
            

            stock_data = yf.download(ticker, start=start_date, end=end_date)

            
            stock_data["Ticker"] = ticker
            stock_data["Company Name"] = company_name

            
            stock_data.to_excel(writer, sheet_name=company_name)
            print(f"Data for {company_name} saved.")

    print(f"All data saved to {output_file}.")

tickers = ["AAPL", "GOOG", "AMZN", "MSFT"]  
company_names = ["APPLE", "GOOGLE", "AMAZON", "MICROSOFT"]
start_date = "2021-01-01"  
end_date = "2024-01-01"    
output_file = "Historical_Stock_Data.xlsx"

stocks_data(tickers, company_names, start_date, end_date, output_file)
