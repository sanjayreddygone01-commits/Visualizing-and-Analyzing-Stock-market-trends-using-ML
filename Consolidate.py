import pandas as pd

def consolidate_stock_data_to_single_sheet(file_path, output_file):

    excel_data = pd.ExcelFile(file_path)
    consolidated_data = pd.DataFrame()

    for sheet_name in excel_data.sheet_names:
        sheet_data = excel_data.parse(sheet_name)
        consolidated_data = pd.concat([consolidated_data, sheet_data], ignore_index=True)

    with pd.ExcelWriter(output_file) as writer:
        consolidated_data.to_excel(writer, index=False, sheet_name='Consolidated Data')

    print(f"Consolidated data saved to {output_file}.")


output_file = "Historical_Stock_Data.xlsx"
consolidated_file = "Consolidated_Stock_Data1.xlsx"

consolidate_stock_data_to_single_sheet(output_file, consolidated_file)
