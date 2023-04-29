employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for employ in employees:
    if employ["vaccinated"]:
        vaccinated.append(employ["fio"])
    else:
        not_vaccinated.append(employ["fio"])

print("Вакцинированные:")
for vaccinat in vaccinated:
    print(vaccinat)

print("Остальные:")
for not_vaccinat in not_vaccinated:
    print(not_vaccinat)
