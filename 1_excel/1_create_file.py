from openpyxl import Workbook

wb = Workbook()  # new work book create
ws = wb.active # active sheet get
ws.title = "NadoSheet"
wb.save("sample.xlsx")
wb.close()
