from openpyxl import load_workbook
wb = load_workbook("sample_fumula.xlsx", data_only=True)
ws = wb.active

for row in ws.values:
    for cell in row:
        print(cell)