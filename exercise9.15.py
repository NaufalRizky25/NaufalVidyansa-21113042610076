from random import choice

pool_lotere = [1, 3, 7, 12, 19, 23, 25, 30, 42, 50, 'a', 'b', 'c', 'd', 'e']
my_ticket = [7, 'b', 25, 42]  # Tiket pilihan Anda


def tarik_lotere(pool):
    """Mengambil 4 item acak dari pool tanpa duplikat posisi"""
    pemenang = []
    while len(pemenang) < 4:
        item = choice(pool)
        if item not in pemenang:
            pemenang.append(item)
    return pemenang


jumlah_loop = 0
menang = False

print("Memulai simulasi pencarian tiket pemenang...")

while not menang:
    jumlah_loop += 1
    hasil_undian = tarik_lotere(pool_lotere)

    # Periksa apakah tiket kita cocok (menggunakan set agar urutan tidak masalah)
    if set(my_ticket) == set(hasil_undian):
        menang = True

print(f"Tiket Anda ({my_ticket}) menang setelah ditarik sebanyak {jumlah_loop:,} kali!")
