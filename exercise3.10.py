listnama_kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]

print(listnama_kota)

print("penggunaan fungsi sort secara alphabet: ")
listnama_kota.sort()
print(listnama_kota)

print("penggunaan fungsi sort secara non alphabet: ")
listnama_kota.sort(reverse=True)
print(listnama_kota)

print("penggunaan fungsi reverse untuk membalikkan urutan list")
listnama_kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]
listnama_kota.reverse()
print(listnama_kota)

print("penggunaan fungsi len untuk menghitung jumlah yang berada di dalamlist")
print(len(listnama_kota))
