myPizza = ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]
friendPizza = myPizza[:]

myPizza.append("Meatlover")
friendPizza.append("Supreme")

for my in myPizza:
    print(my)

for frnd in friendPizza:
    print(frnd)
