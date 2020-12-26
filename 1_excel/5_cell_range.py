from openpyxl import Workbook
from random import *
wb = Workbook()
ws = wb.active

ws.append(["번호", "영어", "수학"])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

# if english teacher
col_B = ws["B"]
#print(col_B)

print("==========get BCol===============")
for cell in col_B:
    print(cell.value)

print("==========get Cols===============")
col_range = ws["B:C"]
for cols in col_range:
    for cell in cols:
        print(cell.value)

print("==========get Title===============")
row_title = ws[1]
for cell in row_title:
    print(cell.value)

print("==========get Rows================")
row_range = ws[2:6]
for rows in row_range:

    for cell in rows:
        print(cell.value, end=" ")
    print()


#wb.save("sample4.xlsx")
