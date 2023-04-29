class Question:

    def __init__(self, text_question, diff_question, good_answer):
        self.text_question = text_question
        self.diff_question = diff_question
        self.good_answer = good_answer
        self.have_question = False
        self.user_answer = None
        self.score_question = int(diff_question) * 10

    def get_points(self):

        """Возвращает int, количество баллов.
         Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self.score_question

    def is_correct(self):

        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        if self.user_answer == self.good_answer:
            return True
        else:
            return False

    def build_question(self):

        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.text_question}\nСложность {self.diff_question}/5"

    def build_positive_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        """

        return f"Ответ верный, получено {self.score_question} баллов"

    def build_negative_feedback(self):

        """Возвращает :
        Ответ неверный, верный ответ __
        """

        return f"Ответ неверный, верный ответ {self.good_answer}"
