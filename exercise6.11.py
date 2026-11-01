cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10000000,
        'fact': 'ibu kota negara ini'
    },
    'bandung': {
        'country': 'indonesia',
        'population': 2500000,
        'fact': 'kota kembang'
    },
    'surabaya': {
        'country': 'indonesia',
        'population': 2700000,
        'fact': 'kota perjuangan'
    }
}

for city, cities_info in cities.items():
    print(f"Kota: {city.title()}:")
    negara = cities_info['country']
    populasi = cities_info['population']
    fakta = cities_info['fact']
    print(f"\tNegara: {negara.title()}")
    print(f"\tPopulasi: {populasi}")
    print(f"\tFakta: {fakta}")
