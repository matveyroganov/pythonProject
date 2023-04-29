class BasicWord:

    def __init__(self, source_words, subwords):

        """Создаем поля: исходное слово и набор допустимых подслов
        """

        self.source_words = source_words
        self.subwords = subwords

    def check_input_word(self, input_word):

        """Проверяем введенное слово в списке допустимых подслов (возвращаем bool)
        """

        if input_word in self.subwords:
            return True
        else:
            return False

    def count_numbers_subwords(self):

        """Подсчитываем количество подслов (возвращаем int)
        """

        return len(self.subwords)

    def count_min_word_len(self):

        """Подсчитываем минимальную длину слова из списка подслов (возвращаем int)
        """

        len_word = []
        for word in self.subwords:
            len_word.append(len(word))
        return min(len_word)

    def __repr__(self):

        """Печатаем исходное слово
        """

        return f"{self.source_words.upper()}"
