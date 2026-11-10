filenames = ["exercise10.8(cat).txt", "exercise10.8(dog).txt"]

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents, end="")

    except FileNotFoundError:
        pass
