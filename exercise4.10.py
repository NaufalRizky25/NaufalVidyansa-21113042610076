kubik = [kubik**3 for kubik in range(1, 10)]


print("Berikut merupakan 3 bilangan kubik pertama: ")
for bilangan in kubik[:3]:
    print(bilangan)

print("Berikut merupakan 3 bilangan kubik dari tengah: ")
for bilangan in kubik[3:6]:
    print(bilangan)

print("Berikut merupakan 3 bilangan kubik dari belakang: ")
for bilangan in kubik[6:9]:
    print(bilangan)
