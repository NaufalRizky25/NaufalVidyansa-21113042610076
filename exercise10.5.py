names = []

while True:
    name = input("Please enter your name (or 'quit' to stop): ")

    if name == 'quit':
        break

    names.append(name)

with open("exercise10.5.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("All names have been saved to exercise10.5.txt!")
