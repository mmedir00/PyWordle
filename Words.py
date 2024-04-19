import random
from Color import *
import time


class Word:
    def __init__(self, language: int, day_word: bool) -> None:
        if language == 1:
            self.file_path = "etc/words-EN.txt"
        else:
            self.file_path = "etc/words-ES.txt"

        if day_word:
            self.word = self.day_word(language)
        else:
            self.word = self.random_word(language)

    def __eq__(self, value: str) -> bool:
        return self.word == value.lower()

    def __str__(self):
        return self.word

    def day_word(self, language: int) -> str:
        if language == 1:
            words_number = 14752
        else:
            words_number = 10130
        seed = ((time.localtime().tm_yday - 1) * time.localtime().tm_year) % words_number
        with open(self.file_path, "r") as file:
            word = file.readlines()[seed]
        return word

    def random_word(self, language: int) -> str:
        with open(self.file_path, "r") as words:
            array = words.readlines()
        return random.choice(array)

    def search(self, letter: str, word: [str]) -> int:
        for i in range(len(word)):
            if letter == word[i]:
                return i

    def verify(self, input_word: str) -> str:
        input_list = list(input_word)
        word_list = list(self.word)
        string = ["", "", "", "", ""]
        green_list = word_list

        for i in range(5):
            if input_list[i] == green_list[i]:
                string[i] = Color.green(input_list[i])
                green_list[i] = " "

        for i in range(5):
            if input_list[i] in green_list and string[i] != Color.green(input_list[i]):
                string[i] = Color.yellow(input_list[i])
                green_list[self.search(input_list[i], green_list)] = " "

        for i in range(5):
            if string[i] == "":
                string[i] = Color.grey(input_list[i])

        return "".join(string)
