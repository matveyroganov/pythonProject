import requests
import random
from basic_word import BasicWord

URL_WORDS = "https://api.jsonserve.com/52loES"


def load_random_word() -> BasicWord:

    """Получаем список слов с внешнего ресурса, выбираем случайное слово, создаем экземпляр класса BasicWord,
       возвращаем этот экземпляр.
    """

    response = requests.get(URL_WORDS)
    list_words = response.json()
    random_word = random.choice(list_words)
    basic_word = BasicWord(random_word["word"], random_word["subwords"])
    return basic_word
