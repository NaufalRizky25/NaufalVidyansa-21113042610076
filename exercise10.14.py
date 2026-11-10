import json

filename = "username.json"


def get_new_username():
    username = input("What is your name? ")

    with open(filename, "w") as file:
        json.dump(username, file)

    return username


def greet_user():
    try:
        with open(filename) as file:
            username = json.load(file)

    except FileNotFoundError:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

    else:
        correct = input(f"Are you {username}? (yes/no): ")

        if correct.lower() == "yes":
            print(f"Welcome back, {username}!")

        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


greet_user()
