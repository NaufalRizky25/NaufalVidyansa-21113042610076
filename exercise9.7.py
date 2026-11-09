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

class Admin(User):
    def __init__(self, namadepan, namabelakang, username, email, lokasi):
        super().__init__(namadepan, namabelakang, username, email, lokasi)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Hak akses (Privileges) untuk Admin {self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_1 = Admin("Andi", "Wijaya", "andi_admin", "andi@email.com", "Surabaya")
admin_1.greetuser()
admin_1.show_privileges()
