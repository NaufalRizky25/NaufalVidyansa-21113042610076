class Restoran:
    def __init__(self, namarestoran, namahidangan):
        self.namarestoran = namarestoran
        self.namahidangan = namahidangan

    def describerestoran(self):
        print(f"{self.namarestoran}, salah satu restoran yang menyediakan hidangan {self.namahidangan} di Indonesia")

    def openrestoran(self):
        print(f"{self.namarestoran}, saat ini sudah dibuka dan bisa dikunjungi\n")


restoran_1 = Restoran("Sederhana", "Nasi Padang")
restoran_2 = Restoran("Bakso Titoti", "Bakso & Mie Ayam")
restoran_3 = Restoran("Sushi Tei", "Makanan Jepang")

restoran_1.describerestoran()
restoran_2.describerestoran()
restoran_3.describerestoran()