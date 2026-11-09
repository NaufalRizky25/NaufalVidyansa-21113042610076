import openpyxl as pxl
FILE_NAME = 'Nilai_Kelas_A.xlsx'
wb = pxl.load_workbook(FILE_NAME, data_only=True)
sheets = wb["Nilai A"]
for row in sheets.iter_rows(min_row=2, max_row=10, min_col=1, max_col=5, values_only=True):
    print([cell for cell in row])
