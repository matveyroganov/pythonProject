from player import Player
from utils import load_random_word


def main():

    final_word = '"stop"'

    # Получаем у пользователя его имя

    print("Введите имя пользователя")

    user_input = input()

    # Создаем экземпляр класса Player с нужным именем.

    name_player = Player(user_input)

    # Здороваемся с пользователем.

    print(f"Привет, {name_player}!")

    # Выводим значение слова из экземпляра, который получили ранее из функции load_random_word

    word = load_random_word()

    # Предлагаем сделать первый ход.

    print(f"Составьте {word.count_numbers_subwords()} слов из слова {word}")
    print(f"Слова должны быть не короче {word.count_min_word_len()} букв")
    print(f"Чтобы закончить игру, угадайте все слова или напишите {final_word}")
    print(f"Поехали, ваше первое слово?")

    # Запускаем цикл, пока количество угаданных слов не сравняется с количеством слов, которые можно составить.

    while name_player.get_numbers_used_words() != word.count_numbers_subwords():

        # В каждой итерации получаем от пользователя слово, выполняем несколько проверок

        word_input = input("Ваше слово: ").lower()

        # Если слово короткое – это неудачное слово.

        if len(word_input) < word.count_min_word_len():
            print(f"Cлишком короткое слово")

        # Если слово уже было угадано пользователем (Player) – это неудачное слово.

        elif name_player.check_used_input_word(word_input):
            print("Слово уже использовано")

        # Если слово stop или стоп, то игра прекращается. Выводим статистику

        elif word_input == "stop" or word_input == "стоп":
            print(f"Игра завершена, количество угаданных слов: {name_player.get_numbers_used_words()}")
            break

        # Если слова нет в списке допустимых у BasicWord – это неудачное слово.

        elif not word.check_input_word(word_input):
            print("Неверное слово")

        # Если все проверки выше пройдены, то слово хорошее, его нужно добавить в
        # список использованных слов класса Player и вывести оповещение об этом пользователю:

        else:
            name_player.add_word_in_used_word(word_input)
            print("Верно")

    # Если все слова отгаданы, выводим финальное сообщение

    else:
        print("Ура! Вы отгадали все слова! Вы молодец! Игра окончена. Всего доброго!")


main()
