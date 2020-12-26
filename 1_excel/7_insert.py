from openpyxl import load_workbook
wb = load_workbook("sample4.xlsx")
ws = wb.active

# ws.insert_rows(8)
# ws.insert_rows(8, 5)

# ws.insert_cols(2)
ws.insert_cols(2, 3)
wb.save("sample4_inert_cols.xlsx")
