def make_sandwich(*items):

    print("\n--- Ringkasan Pesanan Sandwich ---")
    print("Membuat sandwich dengan bahan-bahan berikut:")

    for item in items:
        print(f"- {item}")

    print("Sandwich Anda sedang disiapkan dan siap dinikmati!")


make_sandwich('keju', 'daging sapi', 'tomat')

make_sandwich('selai kacang', 'selai stroberi')

make_sandwich('ayam', 'keju', 'selada', 'mayones', 'saus tomat')
