
pets = [
    {
        "name": "Buddy",
        "kind": "dog",
        "breed": "Golden Retriever",
        "age": 3,
        "owner": "alice",
        "favorite_food": "peanut butter",
       
    },
    {
        "name": "Whiskers",
        "kind": "cat",
        "breed": "Siamese",
        "age": 2,
        "owner": "bob",
        "favorite_food": "tuna",
      
    },
    {
        "name": "Max",
        "kind": "parrot",
        "breed": "Budgie",
        "age": 1,
        "owner": "charlie",
        "favorite_food": "millet seeds",
     
    },
    {
        "name": "Nibbles",
        "kind": "hamster",
        "breed": "Syrian",
        "age": 1,
        "owner": "diana",
        "favorite_food": "sunflower seeds",
      
    }
]

print("🐾 ANIMAL SHELTER PET DIRECTORY 🐾\n" + "="*40)

for pet in pets:
    print(f"\nPet Name: {pet['name']} ({pet['kind'].title()})")
    print(f"  • Breed: {pet['breed']}")
    print(f"  • Age: {pet['age']} year(s) old")
    print(f"  • Owner: {pet['owner'].title()}")
    print(f"  • Favorite Food: {pet['favorite_food'].title()}")
