import openpyxl

def insert_rows(n, m):
    wb = openpyxl.load_workbook('number.xlsx')
    sheet = wb.active
    sheet.insert_rows(n, m)
    wb.save('number.xlsx')

insert_rows(2, 2)
