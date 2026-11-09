from random import choice

pool_lotere = [1, 3, 7, 12, 19, 23, 25, 30, 42, 50, 'a', 'b', 'c', 'd', 'e']

from random import sample
pemenang = sample(pool_lotere, 4)

print("--- Undian Lotere ---")
print(f"Kombinasi angka/huruf yang menang adalah: {pemenang}")
print("Pesan: Tiket apa pun yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")
