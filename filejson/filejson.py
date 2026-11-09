import json

FILE_NAME = 'history_city_list.json'
with open(FILE_NAME, 'r', encoding='latin1') as jsonfile:
    data = json.load(jsonfile)

print(type(data))
print(len(data))

print(data[764])
print(json.dumps(data[764], indent=4))
