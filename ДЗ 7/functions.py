import json

# Заносим файлы в переменные

FILE_PROFESSIONS = "professions.json"
FILE_STUDENTS = "students.json"


def load_students():

    """Загружает список студентов из файла
    """

    path = FILE_STUDENTS

    with open(path, "r", encoding='utf-8') as file:
        json_list = file.read()
        list_students = json.loads(json_list)
    return list_students


def load_professions():

    """Загружает список профессий из файла
    """

    path = FILE_PROFESSIONS

    with open(path, "r", encoding='utf-8') as file:
        json_list = file.read()
        list_professions = json.loads(json_list)
    return list_professions


def get_student_by_pk(pk):

    """	Получает словарь с данными студента по его pk
    """

    list_students = load_students()
    for index in list_students:
        index["pk"] = str(index["pk"])
        if pk == index["pk"]:
            dict_students = {
                "full_name": index["full_name"],
                "skills": index["skills"]
            }
            return dict_students


def get_profession_by_title(title):

    """	Получает словарь с инфо о профе по названию
    """

    list_professions = load_professions()
    for index in list_professions:
        if title == index["title"]:
            dict_professions = {
                "skills": index["skills"]
            }
            return dict_professions


def check_fitness(student, profession):

    """	Получает студента и профессию и возвращает словарь с результатами
    """

    dict_students = get_student_by_pk(student)
    dict_professions = get_profession_by_title(profession)

    skills_student = set(dict_students["skills"])
    skills_profession = set(dict_professions["skills"])

    available_skills = list(skills_profession.intersection(skills_student))
    missing_skills = list(skills_profession.difference(skills_student))
    percent_skills = round((len(available_skills) / len(skills_profession)) * 100)
    dict_results = {
        "has": available_skills,
        "lacks": missing_skills,
        "fit_percent": percent_skills
    }
    return dict_results
