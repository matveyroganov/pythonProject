def read_words(path):

    """Читает слова из файла, формирует список слов  возвращает этот список
    """

    words = []
    with open(path, "r", encoding='utf-8') as file:
        for word in file:
            clear_word = word.strip()
            words.append(clear_word)
        return words


def write_points(name_file, name_player, record):

    """Записывает в файл с историей имя и количество очков
    """

    with open(name_file, "a", encoding='utf-8') as file:
        writing_to_file = file.write(f"{name_player} {record}\n")
    return writing_to_file


def count_statistics(stat):

    """Читает из файла с историей результаты игр и формирует список из количества баллов за все игры
    """

    list_records_players = []
    with open(stat, "r", encoding='utf-8') as file:
        for record in file:
            split_record = record.strip().split(" ")
            clear_record = split_record[-1]
            list_records_players.append(clear_record)
        return list_records_players
