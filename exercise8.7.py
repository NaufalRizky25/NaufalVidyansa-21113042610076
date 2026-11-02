def makeAlbum(penyanyi, namaAlbum, jumlahlagu=None):
    album = {'artis': penyanyi,
             'nama': namaAlbum}
    if jumlahlagu is not None:
        album['lagu'] = jumlahlagu
    return penyanyi, namaAlbum, jumlahlagu


m1 = makeAlbum('The Beatles', 'Abbey Road')
m2 = makeAlbum('Pink Floyd', 'The Dark Side of the Moon', 10)
m3 = makeAlbum('Michael Jackson', 'Thriller', 9)

print(m1)
print(m2)
print(m3)
