tempatfavorit = {
    'naufal': ['pantai', 'gunung'],
    'rizky': ['danau', 'hutan'],
    'vidyansa': ['pantai', 'kolam renang']}

for nama, tempat in tempatfavorit.items():
    print(f"tempat favorit {nama.title()} adalah:")
    for t in tempat:
        print(f"\t{t.title()}")
