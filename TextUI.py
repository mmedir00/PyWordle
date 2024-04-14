import Color
from Game import *


class TextUI:
    def __init__(self) -> None:
        clean()
        print(
            "{0}\nWebScrapping on {1} and {2} for word validation\n{3}".format(Color.purple("--WELCOME TO PYWORDLE!--"),
                                                                               Color.red(
                                                                                   "dle.rae.es"),
                                                                               Color.blue("www.dictionary.com"),
                                                                               Color.grey(
                                                                                   "by @MarcMeRu\n")))
        user_input = int(input("1. English\n2. Español\n3. Quit\n>>> "))
        if user_input == 3:
            exit()
        elif user_input in [1, 2]:
            self.game = Game(user_input)

    def common_game(self):
        self.game.game_loop()

    def difficult_game(self):
        for i in range(3):
            if not self.game.game_loop():
                break

    def hardcore_game(self):
        for i in range(5):
            if not self.game.game_loop():
                break
