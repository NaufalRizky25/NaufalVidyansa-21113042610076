class User:
    def __init__(self, namadepan, namabelakang, username, email, lokasi):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.username = username
        self.email = email
        self.lokasi = lokasi

    def describeuser(self):
        print(f"Ringkasan Profil Pengguna ({self.username}):")
        print(f"- Nama Lengkap: {self.namadepan} {self.namabelakang}")
        print(f"- Email: {self.email}")
        print(f"- Lokasi: {self.lokasi}")

    def greetuser(self):
        print(f"Halo, {self.namadepan} {self.namabelakang}! Senang melihat Anda kembali.")
