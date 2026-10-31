usernames = []

for username in usernames:
    if username == "admin":
        print("hallo admin, apakah kamu ingin melihat status laporan")
    else:
        print(f"hallo, {username}, selamat datang kembali")

if len(usernames) == 0:
    print("Kita harus mencari pengguna baru")
