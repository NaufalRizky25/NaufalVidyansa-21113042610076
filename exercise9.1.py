class Restoran:
    def __init__(self, namarestoran, namahidangan):
        self.namarestoran = namarestoran
        self.namahidangan = namahidangan

    def describerestoran(self):
        print(f"{self.namarestoran}, salah satu restoran yang menyediakan hidangan {self.namahidangan} di Indonesia")


    def openrestoran(self):
        print(f"{self.namarestoran}, saat ini sudah dibuka dan bisa dikunjungi")


RestoranFvrt = Restoran("Warteg", "tempe orek")

RestoranFvrt.describerestoran()
RestoranFvrt.openrestoran()
