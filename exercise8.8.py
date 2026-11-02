def makeAlbum(penyanyi, namaAlbum, jumlahlagu=None):
    album = {'artis': penyanyi,
             'nama': namaAlbum}
    if jumlahlagu is not None:
        album['lagu'] = jumlahlagu
    return album


while True:
    print("\n Harap memasukkan data Album: ")
    print("Ketik q jika sudah selesai, terimakasih!")

    artis = input("Masukkan nama artis: ")
    if artis == "q":
        break

    judul = input("Masukkan judul album: ")
    if judul == "q":
        break

albumInfo = makeAlbum()
print(albumInfo)
