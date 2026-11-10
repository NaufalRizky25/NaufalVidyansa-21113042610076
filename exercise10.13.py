import json

username = input("What is your username? ")
age = input("How old are you? ")
favorite_color = input("What is your favorite color? ")

user_info = {
    "username": username,
    "age": age,
    "favorite_color": favorite_color
}

filename = "user_info.json"

with open(filename, "w") as file:
    file.write(json.dumps(user_info))

with open(filename) as file:
    contents = file.read()

remembered_info = json.loads(contents)

print("\nHere's what I remember about you:")
print(f"Username: {remembered_info['username']}")
print(f"Age: {remembered_info['age']}")
print(f"Favorite color: {remembered_info['favorite_color']}")
