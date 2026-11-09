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


user_1 = User("Budi", "Santoso", "budisantoso", "budi@email.com", "Jakarta")
user_2 = User("Siti", "Aisyah", "sitiaisyah", "siti@email.com", "Bandung")
user_3 = User("Rian", "Pratama", "rian_p", "rian@email.com", "Surabaya")


for user in [user_1, user_2, user_3]:
    user.greetuser()
    user.describeuser()
