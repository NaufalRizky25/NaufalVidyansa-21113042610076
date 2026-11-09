class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Mobil ini memiliki jarak tempuh {self.odometer_reading} mil.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Anda tidak dapat memutar balik odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self) :
        if self.battery_size == 40:
            range_distance = 150
        elif self.battery_size == 65:
            range_distance = 225

        print(f"Mobil ini dapat menempuh jarak sekitar {range_distance} mil dengan baterai penuh.")

    def upgrade_battery(self):
        """Memeriksa kapasitas baterai dan mengubahnya menjadi 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai telah di-upgrade ke kapasitas 65 kWh.")
        else:
            print("Baterai sudah memiliki kapasitas maksimum.")


class ElectricCar(Car):
    """Aspek khusus dari mobil listrik, mewarisi dari kelas Car."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("\n--- Melakukan Upgrade Baterai ---")
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
