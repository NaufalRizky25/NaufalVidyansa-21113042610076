
print("Reading the entire file:")

with open("exercise10.1.txt") as file:
    contents = file.read()
    print(contents, end="")


print("\nReading lines from a list:")

with open("exercise10.1.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")
