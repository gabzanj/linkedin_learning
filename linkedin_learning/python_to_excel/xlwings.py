import xlwings as xw

path_files = r'..\PycharmProjects\linkedin_learning\python_to_excel\files'
wb = xw.Book(f'{path_files}\\Notas.xlsx')

sheet_name = wb.sheets(1).name
ws = wb.sheets(1)
wb.close()

new_wb = xw.Book()

text = 'Writing data in cell A1 of worksheet 1'
new_wb.sheets(1).range('A1').value = text

ws = new_wb.sheets(1)
ws.range('A2').value = 'How to manipulate cells with xlwings'

ws.range('A1:D1').merge()
ws.range('A2:G2').merge()

ws.range('A1:G2').color = '#548235'
ws.range('A1:G2').font.color = '#FFFFFF'
ws.range('A1:G2').font.bold = True

titles = ['ITEM', 'PRODUCT', 'UNIT PRICE', 'TOTAL']
items = ([1, 'Peoduct 1', 100], [2, 'Product 2', 300],
         [3, 'Product 3', 145], [4, 'Product 4', 500])

ws.range('A4:D4').value = titles
ws.range('A5:D7').value = items
ws.used_range.autofit()

new_wb.save(f'{path_files}\\New_notas.xlsx')
new_wb.close()
