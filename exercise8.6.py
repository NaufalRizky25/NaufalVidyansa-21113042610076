def kotanegara(kota, negara):
    nama = f"{kota}, {negara}"
    return nama.title()


namakota = kotanegara("jakarta", "indonesia")
print(namakota)

namakota = kotanegara("bandung", "indonesia")
print(namakota)

namakota = kotanegara("Surabaya", "indonesia")
print(namakota)
