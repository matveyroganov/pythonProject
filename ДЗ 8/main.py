import random
from methods import Question
from functions import load_questions, count_statistic


def main():

    # Начинаем игру

    print("Игра начинается!\n")

    # Загружаем список и перемешиваем его

    list_questions = load_questions()
    random.shuffle(list_questions)

    questions = []
    number_scores = 0

    # Проходим циклом по списку вопросов

    for dictionary in list_questions:

        # Выводим класс вопросов

        question = Question(dictionary["q"], dictionary["d"], dictionary["a"])

        # Складываем экземпляры класса в список

        list_exemplars = [dictionary["q"], dictionary["d"], dictionary["a"]]
        questions.append(list_exemplars)

        # Выводим вопросы

        print(question.build_question())

        # Пользователь вводит свой ответ на вопрос

        question.user_answer = input()

        # Проверяем корректность ответа

        if question.is_correct():
            print(question.build_positive_feedback())
            list_exemplars.append(True)
            number_scores += question.get_points()
        else:
            print(question.build_negative_feedback())
            list_exemplars.append(False)

    # Выводим статистику ответов

    correct_answers = count_statistic(questions)
    print(correct_answers)
    print(f"Набрано баллов: {number_scores}")


main()
