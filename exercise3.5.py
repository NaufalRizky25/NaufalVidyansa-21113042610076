listnama = ["Iyan", "Akbar", "Fayaz", "Abi"]
print(listnama)

for i in range(len(listnama)):
    print(f"Hello {listnama[i]}, saya mengundang anda untuk hadir di acara ulang tahun saya.")

# Akbar tidak bisa hadir di acara ulang tahun saya
print(f"Aku dengar {listnama[1]} tidak bisa hadir")

del listnama[1]

listnama.insert(1, "Jude")

print(listnama)

for i in range(len(listnama)):
    print(f"Hello {listnama[i]}, saya mengundang anda untuk hadir di acara ulang tahun saya.")
