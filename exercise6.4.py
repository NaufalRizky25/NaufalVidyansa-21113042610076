gloossary = {
    'list': 'sebuah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel',
    'dictionary': 'sebuah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel, tetapi menggunakan pasangan key-value',
    'tuple': 'sebuah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel, tetapi tidak dapat diubah setelah dibuat',
    'set': 'sebuah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel, tetapi tidak memiliki urutan dan tidak dapat diubah setelah dibuat',
    'string': 'sebuah tipe data yang digunakan untuk menyimpan teks'}

for key, value in gloossary.items():
    print(f"{key.title()} adalah {value}")

gloossary['integer'] = 'sebuah tipe data yang digunakan untuk menyimpan bilangan bulat'
gloossary['float'] = 'sebuah tipe data yang digunakan untuk menyimpan bilangan desimal'
gloossary['boolean'] = 'sebuah tipe data yang digunakan untuk menyimpan nilai True atau False'
gloossary['complex'] = 'sebuah tipe data yang digunakan untuk menyimpan bilangan kompleks'
gloossary['bytes'] = 'sebuah tipe data yang digunakan untuk menyimpan data biner'

print("\nSetelah menambahkan beberapa istilah baru:")
for key, value in gloossary.items():
    print(f"{key.title()} adalah {value}")
