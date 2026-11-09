import pandas as pd

FILECSV = 'nilaikuliah.csv'

dfCSV = pd.read_csv(FILECSV, delimiter=',', encoding='latin1')
print(dfCSV.describe())
dfCSV.to_csv('nilaikuliah.csv', sep=';', index=False)

df_excel = pd.read_excel("readexcel/Nilai_KelasA.xlsx", sheet_name='Nilai_A')
print(df_excel.describe())