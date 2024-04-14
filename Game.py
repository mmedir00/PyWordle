from Words import *
from Color import *
from WordValidator import *
import os


def clean() -> None:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


class Game:
    def __init__(self, language: int) -> None:
        self.word: Word = Word(language)
        self.validator = WordValidator(language)
        self.language: int = language
        self.tries: int = 0
        self.guessed = False
        self.texts = {
            "Intro": {1: "Try to guess the secret word!\n5 letters, 5 attempts.\n",
                      2: "Intente adivinar la palabra secreta!\n5 letras, 5 intentos.\n"},

            "Attempt": {1: "Attempt number ",
                        2: "Intento número "},

            "LengthError": {1: "The word must have 5 letters.",
                            2: "La palabra debe tener 5 letras."},

            "DictError": {1: "The word doesn't exist in the dictionary.",
                          2: "La palabra no existe en el diccionario."},

            "Won": {1: "Congratulations! You won!",
                    2: "¡Felicidades! ¡Ganaste!"},

            "Lost": {1: "You lost! The word was ",
                     2: "¡Perdiste! La palabra era "},

            "Press": {1: "Press enter to continue...",
                      2: "Presione enter para continuar..."}
        }

    def game_loop(self) -> bool:
        clean()
        print(self.texts["Intro"][self.language])

        while not self.guessed and self.tries < 5:
            print(self.texts["Attempt"][self.language] + Color.blue(str(self.tries)) + ".")
            guess: str = input(">>> \r")

            if not self.validator.validate_length(guess):
                print(f">>> {Color.red(guess)}")
                print(self.texts["LengthError"][self.language])

            elif not self.validator.validate_dictionary(guess):
                print(f">>> {Color.red(guess)}")
                print(self.texts["DictError"][self.language])

            elif guess == self.word:
                print(f">>> {Color.green(guess)}")
                print(self.texts["Won"][self.language])
                self.guessed = True

            else:
                print(f">>> {self.word.verify(guess)}\n")
                self.tries += 1

        if not self.guessed:
            print(self.texts["Lost"][self.language] + Color.red(str(self.word)) + ".")

        return self.guessed

