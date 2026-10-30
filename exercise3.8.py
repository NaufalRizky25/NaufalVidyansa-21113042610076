listTempat = ["Jakarta", "Bandung", "Surabaya", "Medan", "Makassar", "Bali", "Yogyakarta", "Semarang", "Solo", "Malang"]

print("list original:")
print(listTempat)

print("\nlist setelah diurutkan alphabetically:")
listTempat.sort()
print(listTempat)

print("\nlist original kembali:")
print(listTempat)

print("\nlist setelah diurutkan secara non alphabetical:")
listTempat.sort(reverse=True)
print(listTempat)

print("\nlist original kembali:")
print(listTempat)

print("\nlist setelah diurutkan secara terbalik:")
listTempat.reverse()
print(listTempat)

print("\nlist setelah diurutkan secara terbalik kembali:")
listTempat.reverse()
print(listTempat)

listTempat.reverse()
print("\nlist setelah dilakukan reverse dan diurutkan secara alphabetical:")
print(sorted(listTempat))

print("\nlist setelah dilakukan reverse diurutkan secara non alphabetical:")
print(sorted(listTempat, reverse=True))