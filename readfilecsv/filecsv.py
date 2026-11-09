import csv
FILE_NAME = 'nilaikuliah.csv'
listNilai = []

with open(FILE_NAME) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0

    for baris in readCSV:
        if line_count == 0:
            print(f"Nama kolom : {baris}")
            line_count += 1
        else:
            print(baris)
            listNilai.append(baris)
            line_count += 1
    print(f'Total {line_count} baris')

csvfile.close()
print('isi nested list yang dibuat: ')
print(listNilai)
