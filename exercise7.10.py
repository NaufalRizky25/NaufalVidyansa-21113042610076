prompt = "Jika kamu bisa pergi ke mana saja di dunia, kemana kamu ingin pergi? "

responses = {}
active = True

while active:
    name = input("\nMasukkan nama Anda: ")
    response = input(prompt)

    responses[name] = response

    repeat = input("Apakah ada orang lain yang ingin menjawab? (ya/tidak) ")
    if repeat.lower() == 'tidak':
        active = False

print("\nHasil survei:")
for name, response in responses.items():
    print(f"{name.title()}: {response.title()}")
