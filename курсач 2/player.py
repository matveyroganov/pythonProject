class Player:

    def __init__(self, user_name):

        """Создаем поля: имя пользователя и использованные слова пользователя (пустой список)
        """

        self.user_name = user_name
        self.used_words = []

    def get_numbers_used_words(self):

        """Получаем количество использованных слов (возвращаем int)
        """

        return len(self.used_words)

    def add_word_in_used_word(self, input_word):

        """Добавляем слова в использованные слова (ничего не возвращаем)
        """

        self.used_words.append(input_word)

    def check_used_input_word(self, input_word):

        """Проверяем использование данного слова до этого (возвращает bool).
        """

        if input_word in self.used_words:
            return True
        else:
            return False

    def __repr__(self):

        """Печатаем имя пользователя
        """

        return f"{self.user_name.title()}"
