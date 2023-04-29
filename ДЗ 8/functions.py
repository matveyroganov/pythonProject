import json

# Заносим файлы в переменные

FILE_QUESTIONS = "questions.json"


def load_questions():

    """Загружает список вопросов из файла
    """

    path = FILE_QUESTIONS

    with open(path, "r", encoding='utf-8') as file:
        json_list = file.read()
        json_questions = json.loads(json_list)
    return json_questions


def count_statistic(questions):

    """Считает статистику верных ответов и выводит результат
    """

    good_answers = []
    for i in questions:
        if True in i:
            good_answers.append(True)
    return f"Вот и всё!\nОтвечено {sum(good_answers)} вопроса из {len(questions)}"
