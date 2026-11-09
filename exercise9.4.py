class Restoran:
    def __init__(self, namarestoran, namahidangan):
        self.namarestoran = namarestoran
        self.namahidangan = namahidangan
        self.number_served = 0

    def describerestoran(self):
        print(f"{self.namarestoran}, salah satu restoran yang menyediakan hidangan {self.namahidangan} di Indonesia.")

    def openrestoran(self):
        print(f"{self.namarestoran}, saat ini sudah dibuka dan bisa dikunjungi.")


restaurant = Restoran("Sederhana", "Nasi Padang")


print(f"Jumlah pelanggan yang telah dilayani: {restaurant.number_served}")


restaurant.number_served = 150
print(f"Jumlah pelanggan setelah diperbarui: {restaurant.number_served}")
