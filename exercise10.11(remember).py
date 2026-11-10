import json

filename = "favorite_number.json"

try:
    with open(filename) as file:
        favorite_number = json.load(file)
except FileNotFoundError:
    favorite_number = None

if favorite_number is not None:
    print(f"I know your favorite number! It's {favorite_number}.")
else:
    favorite_number = int(input("What is your favorite number? "))

    with open(filename, "w") as file:
        json.dump(favorite_number, file)

print("Your favorite number has been saved!")
