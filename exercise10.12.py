import json

filename = "favorite_number.json"

try:
    with open(filename) as file:
        favorite_number = json.load(file)

except FileNotFoundError:
    favorite_number = int(input("What is your favorite number? "))

    with open(filename, "w") as file:
        json.dump(favorite_number, file)

    print("I'll remember your favorite number!")

else:
    print(f"I know your favorite number! It's {favorite_number}.")
