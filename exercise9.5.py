class User:
    def __init__(self, namadepan, namabelakang, username, email, lokasi):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.username = username
        self.email = email
        self.lokasi = lokasi
        self.login_attempts = 0  # Atribut dengan nilai default 0

    def describeuser(self):
        print(f"Ringkasan Profil Pengguna ({self.username}):")
        print(f"- Nama Lengkap: {self.namadepan} {self.namabelakang}")
        print(f"- Email: {self.email}")
        print(f"- Lokasi: {self.lokasi}")

    def greetuser(self):
        print(f"Halo, {self.namadepan} {self.namabelakang}! Senang melihat Anda kembali.")

    def increment_login_attempts(self):
        """Menambahkan nilai login_attempts sebanyak 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mereset nilai login_attempts kembali menjadi 0"""
        self.login_attempts = 0


user_1 = User("Budi", "Santoso", "budisantoso", "budi@email.com", "Jakarta")


user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f"Jumlah percobaan login saat ini: {user_1.login_attempts}")


user_1.reset_login_attempts()


print(f"Jumlah percobaan login setelah di-reset: {user_1.login_attempts}")
