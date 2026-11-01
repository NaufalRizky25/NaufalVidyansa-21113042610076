prompt = "Masukkan topping untuk pizza anda, "
prompt += "\nKetik 'selesai' jika sudah selesai menambahkan topping: "

topping = ""
while topping != 'selesai':
    topping = input(prompt)
    if topping != 'selesai':
        print(f"Topping {topping} telah ditambahkan ke pizza Anda.")
    else:
        print("Pizza akan segera disajikan. Terima kasih!")
