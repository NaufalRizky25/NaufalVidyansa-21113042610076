prompt = "Isi umur Anda: (Ketik 'selesai' jika sudah selesai): "

while True:
    umur = input(prompt)
    if umur.lower() == 'selesai':
        break
    umur = int(umur)
    if umur < 3:
        print("Tiket gratis.")
    elif 3 <= umur < 12:
        print("Harga tiket: Rp10.000.")
    else:
        print("Harga tiket: Rp15.000.")
