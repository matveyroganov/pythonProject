order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for name_order in order:
    name_order["skolko"] = int(name_order["skolko"])
    name_order["poroda"] = name_order["poroda"].title()
    name_order["sred_razmer"] = round(name_order["sred_razmer"] / 10)
    name_order["count"] = name_order.pop("skolko")
    name_order["specie"] = name_order.pop("poroda")
    name_order["avg_size"] = name_order.pop("sred_razmer")

# Не удаляйте текст ниже, он нужен для проверки

for item in order:
  for key, value in item.items():
      print(key, value)
