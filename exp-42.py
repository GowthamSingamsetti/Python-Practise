import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook("transactions.xlsx")
sheet = wb['Sheet1']
cell = sheet['a2']
cell = sheet.cell('1, 2')
print(cell.value)

print(sheet.max_row)
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)
    print(cell.value)
    corrected_price = 0.9 * cell.value
    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price


values = Reference(sheet,
                   min_row = 1,
                   max_row = sheet.max_row,
                   min_col = 4,
                   max_col = 4)

chart = BarChart()
chart.add_data(values)
sheet.add_chart
