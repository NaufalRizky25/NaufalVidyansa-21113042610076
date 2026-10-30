listnama = ['Zahir', 'Iyan', 'Akbar', 'Nizar', 'Fayaz', 'Abi', 'Naufal']

print("Mohon maaf, saya hanya bisa mengundang 2 orang saja di acara ulang tahun saya.")

for i in range(5):
    listnama_pop = listnama.pop()
    print(f"Maaf {listnama_pop}, saya tidak bisa mengundang anda di acara ulang tahun saya.")

print(listnama)

for i in range(len(listnama)):
    print(f"hallo {listnama[i]}, saya tetap mengundang anda untuk hadir di acara ulang tahun saya.")

del listnama[0]
del listnama[0]

print(listnama)
