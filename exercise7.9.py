rotibakar = ["roti bakar coklat", "roti bakar keju", "roti bakar selai kacang",
             "roti bakar pisang", "roti bakar sosis",
             "roti bakar coklat", "roti bakar coklat"]
rotibakarjadi = []
print("Maaf untuk sementara roti bakar coklat sedang habis")

while "roti bakar coklat" in rotibakar:
    rotibakar.remove("roti bakar coklat")

while rotibakar:
    rotibakarproses = rotibakar.pop()
    print(f"{rotibakarproses.title()} sedang dipanggang.")
    rotibakarjadi.append(rotibakarproses)

print("\nBerikut adalah roti bakar yang sudah jadi:")
for roti in rotibakarjadi:
    print(f"{roti.title()}")
