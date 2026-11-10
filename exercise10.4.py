name = input("Please enter your name: ")

with open("exercise10.4.txt", "w") as file:
    file.write(name)

print("Your name has been saved!")
