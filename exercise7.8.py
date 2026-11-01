rotibakar = ["roti bakar coklat", "roti bakar keju", "roti bakar selai kacang",
             "roti bakar pisang", "roti bakar sosis"]
rotibakarjadi = []

while rotibakar:
    rotibakarproses = rotibakar.pop()
    print(f"{rotibakarproses.title()} sedang dipanggang.")
    rotibakarjadi.append(rotibakarproses)

print("\nBerikut adalah roti bakar yang sudah jadi:")
for roti in rotibakarjadi:
    print(f"{roti.title()}")
