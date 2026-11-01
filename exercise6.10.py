angkateman = {'naufal': [7, 14], 'rizky': [3, 6], 'vidyansa': [5, 10], 'dimas': [9, 18], 'putra': [1, 2]}

for nama, angka in angkateman.items():
    print(f"Teman saya bernama {nama.title()} dan angka favoritnya adalah:")
    for a in angka:
        print(f"\t{a}")
