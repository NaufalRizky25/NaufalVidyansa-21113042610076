from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dadu_6 = Die(6)
print("--- Lemparan Dadu 6 Sisi (10x) ---")
hasil_6 = [dadu_6.roll_die() for _ in range(10)]
print(hasil_6)

dadu_10 = Die(10)
print("\n--- Lemparan Dadu 10 Sisi (10x) ---")
hasil_10 = [dadu_10.roll_die() for _ in range(10)]
print(hasil_10)

dadu_20 = Die(20)
print("\n--- Lemparan Dadu 20 Sisi (10x) ---")
hasil_20 = [dadu_20.roll_die() for _ in range(10)]
print(hasil_20)
