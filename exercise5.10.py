usernames = ["nopal", "akbar", "iyan", "fayaz", "admin"]

newusernames = ["Nopal", "AKBAR", "abi", "rizky", "vidyansa"]

for name in newusernames:
    if name.lower() in usernames or name.capitalize() in usernames or name.title() in usernames:
        print(f"Nama pengguna {name} telah digunakan, harap untuk memasukkan username lain")
    else:
        print(f"Nama pengguna {name} tersedia")
