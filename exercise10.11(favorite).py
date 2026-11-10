import json

filename = "favorite_number.json"

with open(filename) as file:
    favorite_number = json.loads(file.read())

print(f"I know your favorite number! It's {favorite_number}.")
