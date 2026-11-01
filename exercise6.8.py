pet1 = {'jenis': 'kucing', 'pemilik': 'naufal'}
pet2 = {'jenis': 'anjing', 'pemilik': 'rizky'}
pet3 = {'jenis': 'burung', 'pemilik': 'vidyansa'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Jenis hewan peliharaan: {pet['jenis']}, Pemilik: {pet['pemilik']}")