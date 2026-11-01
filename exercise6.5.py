sungai = {'nil': 'mesir', 'amazon': 'brazil', 'bengawan solo': 'indonesia', 'yangtze': 'cina', 'mississippi': 'amerika serikat'}

for key, value in sungai.items():
    print(f"Sungai {key.title()} berada di {value.title()}")

for key in sungai.keys():
    print(f"Sungai {key.title()}")
  
for value in sungai.values():
    print(f"Negara {value.title()}")
