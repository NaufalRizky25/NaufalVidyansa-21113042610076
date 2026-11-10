with open("exercise10.1.txt") as file:
    for line in file:
        modified_line = line.replace("Python", "Java")
        print(modified_line, end="")
