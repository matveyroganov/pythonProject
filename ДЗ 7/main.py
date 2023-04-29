from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    # Программа просит ввести номер студента

    number_student = input("Введите номер студента\n")
    dict_student = get_student_by_pk(number_student)

    # Программа проверяет условие ввода номера студента

    if dict_student is None:
        print("У нас нет такого студента")
        return

    # Если номер студента совпадает с номером из файла, программа печатает имя студента и список скиллов

    student = dict_student["full_name"]
    skills_student = ', '.join(dict_student['skills'])
    print(f"Студент {student}\nЗнает {skills_student}")

    # Программа просит ввести специальность

    print(f"Выберите специальность для оценки студента {student}")
    profession = input().title()
    dict_profession = get_profession_by_title(profession)

    # Программа проверяет введенную специальность

    if dict_profession is None:
        print("У нас нет такой специальности")
        return

    # Если введенная спецаильность совпадает со специальностью из файла, то программа выдает результаты

    results = check_fitness(number_student, profession)
    student_knows = ", ".join(results["has"])
    student_doesnt_knows = ", ".join(results["lacks"])

    print(
        f"Пригодность {results['fit_percent']}\n{student} знает {student_knows}"
        f"\n{student} не знает {student_doesnt_knows}"
    )


main()
