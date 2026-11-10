with open("exercise10.1.txt") as file:
    contents = file.read()

for line in contents.splitlines():
    print(line)
