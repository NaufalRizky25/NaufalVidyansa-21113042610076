listnama = ["Iyan", "Akbar", "Fayaz", "Abi"]
print(listnama)

#masih ingin mengundang 3 orang lagi
listnama.insert(0, "Zahir")
listnama.insert(3, "Nizar")
listnama.append("Naufal")

print(listnama)

for i in range(len(listnama)):
    print(f"Hello {listnama[i]}, saya mengundang anda untuk hadir di acara ulang tahun saya.")