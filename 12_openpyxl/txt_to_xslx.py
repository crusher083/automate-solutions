import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active


def txt_to_xlsx(*args):
    j = 0
    for n in args:
        j += 1
        with open(n, 'r') as f:
            rows = [line.rstrip() for line in f]
            for i in range(1, len(rows) + 1):
                sheet.cell(row=i, column=j).value = rows[i - 1]


txt_to_xlsx('xlsx1.txt', 'xlsx2.txt')
wb.save('new_xlsx.xlsx')