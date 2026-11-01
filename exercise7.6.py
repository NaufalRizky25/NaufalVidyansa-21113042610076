prompt = "Isi umur Anda: (Ketik 'selesai' jika sudah selesai): "
# menggunakan exit conditional statement
umur = ""
while umur != 'selesai':
    umur = input(prompt)
    if umur != 'selesai':
        umur = int(umur)
        if umur < 3:
            print("Tiket gratis.")
        elif 3 <= umur < 12:
            print("Harga tiket: Rp10.000.")
        else:
            print("Harga tiket: Rp15.000.")

print("Terima kasih telah membeli tiket. Selamat menikmati pertunjukan!")

# menggunakan exit flag
active = True

while active:
    umur = input(prompt)
    if umur == "selesai":
        active = False
    else:
        umur = int(umur)
        if umur < 3:
            print("Tiket gratis.")
        elif 3 <= umur < 12:
            print("Harga tiket: Rp10.000.")
        else:
            print("Harga tiket: Rp15.000.")


#menggunakan break statement
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
