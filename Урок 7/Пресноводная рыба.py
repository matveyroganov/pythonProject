fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for fishes in fish:
    if fishes["water"] == "fresh":
        fresh_water.append(fishes["specie"])
    elif fishes["water"] == "sea":
        sea_water.append(fishes["specie"])

fishes_fresh_water = ", ".join(fresh_water)
fishes_sea_water = ", ".join(sea_water)

print(f"Морские: {fishes_sea_water}")
print(f"Пресноводные: {fishes_fresh_water}")
