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

            "Attempt": {1: "Attempt number {0}.",
                        2: "Intento número {0}."},

            "LengthError": {1: Color.red("\nThe word must have 5 letters.\n"),
                            2: Color.red("\nLa palabra debe tener 5 letras.\n")},

            "DictError": {1: Color.red("\nThe word doesn't exist in the dictionary.\n"),
                          2: Color.red("\nLa palabra no existe en el diccionario.\n")},

            "Won": {1: Color.green("Congratulations! You won!"),
                    2: Color.green("¡Felicidades! ¡Ganaste!")},

            "Lost": {1: Color.red("You lost! The word was {0}."),
                     2: Color.red("¡Perdiste! La palabra era {0}.")},

            "Press": {1: Color.purple("Press enter to continue..."),
                      2: Color.purple("Presione enter para continuar...")}
        }

    def game_loop(self) -> bool:
        clean()
        print(self.texts["Intro"][self.language])

        while not self.guessed and self.tries < 5:
            print(self.texts["Attempt"][self.language].format(Color.blue(str(self.tries + 1))))
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
            print(self.texts["Lost"][self.language].format(Color.red(str(self.word))))

        return self.guessed

