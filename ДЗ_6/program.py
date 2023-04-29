import random

"""Импортируем функции из отдельного файла
"""

from function import read_words, write_points, count_statistics


def main():

    """Записываем константы подсчета очков
    """

    points_count = 10
    points_record = 0

    """Ввод имени пользователя
    """

    print('Введите ваше имя')
    user_name = input().strip().title()

    """Запускаем функцию считывания слов из файла
    """

    list_words = read_words("words.txt")

    """Запускаем цикл по списку слов из файла
    """

    for word in list_words:

        """Перемешиваем буквы в слове из списка
        """

        split_word = list(word)
        random.shuffle(split_word)
        mix_word = "".join(split_word)

        """Игрок вводит ответ
        """

        print(f"Угадайте слово: {mix_word}")
        word_input = input().lower()

        """Проверяем условие, совпадает ли введенное слово со словом из списка
        """

        if word != word_input:
            print(f"Неверно! Верный ответ – {word}")
        else:
            print(f"Верно! Вы получаете {points_count} очков")
            points_record += points_count

    """Записываем результат в файл
    """

    write_points("history.txt", user_name, points_record)

    """Выводим общую статистику за все игры
    """

    print_statistic = count_statistics("history.txt")

    print(f"Всего игр сыграно: {len(print_statistic)}")
    print(f"Максимальный рекорд: {max(print_statistic)}")

main()