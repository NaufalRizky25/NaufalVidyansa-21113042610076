favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python'}

friends = ['phil', 'sarah', 'naufal', 'rizky', 'edward']

for name in friends:
    if name not in favorite_languages:
        print(f"Harap untuk mengisi data bahasa pemrograman favorit Anda, {name.title()}.")
    else:
        print(f"Terima kasih {name.title()} telah mengisi data bahasa pemrograman favorit Anda.")
