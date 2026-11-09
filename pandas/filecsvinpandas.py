import pandas as pd

FILECSV = 'prokomnaufal/nilaikuliah.csv'

dfCSV = pd.read_csv(FILECSV, delimiter=',', encoding='latin1')
print(dfCSV.head())
