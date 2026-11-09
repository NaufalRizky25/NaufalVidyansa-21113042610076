class Restoran:
    def __init__(self, namarestoran, namahidangan):
        self.namarestoran = namarestoran
        self.namahidangan = namahidangan

    def describerestoran(self):
        print(f"{self.namarestoran}, salah satu restoran yang menyediakan hidangan {self.namahidangan} di Indonesia.")

    def openrestoran(self):
        print(f"{self.namarestoran}, saat ini sudah dibuka dan bisa dikunjungi.")

class IceCreamStand(Restoran):
    def __init__(self, namarestoran, namahidangan="Es Krim"):
        super().__init__(namarestoran, namahidangan)
        self.flavors = ["Cokelat", "Vanila", "Strawberry", "Matcha", "Mangga"]

    def display_flavors(self):
        print(f"Daftar rasa es krim di {self.namarestoran}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


es_krim_enak = IceCreamStand("Gelato Corner")
es_krim_enak.describerestoran()

es_krim_enak.display_flavors()
