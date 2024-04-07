from Words import *
from WordValidator import *
import os


class TextUI:
    def __init__(self) -> None:
        self.clean()
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
            self.game_loop(user_input)

    def game_loop(self, language: int) -> None:
        while True:
            original_word = Word(language)
            validator = WordValidator(language)
            counter = 0
            guessed = False

            self.clean()
            if language == "1":
                print("Try to guess the secret word!\n5 letters, 5 attempts\n")
            elif language == "2":
                print("Intente adivinar la palabra secreta!\n5 letras, 5 intentos\n")

            while counter < 5 and not guessed:

                if language == "1":
                    user_input = str(input("\nAttempt " + Color.blue(str(counter + 1)) + "\n>>> "))
                else:
                    user_input = str(input("\nIntento " + Color.blue(str(counter + 1)) + "\n>>> "))

                if not validator.validate_length(user_input):
                    if language == "1":
                        print(Color.red("The word must have 5 letters"))
                    else:
                        print(Color.red("La palabra debe tener 5 letras"))

                elif not validator.validate_dictionary(user_input):
                    if language == "1":
                        print(Color.red("The word doesn't exist in the dictionary."))
                    else:
                        print(Color.red("La palabra no existe en el diccionario."))

                elif user_input == original_word:
                    if language == "1":
                        input(f"<<< {Color.green(user_input)}\nCongratulations! You won!\nPress enter to continue...")
                    else:
                        input(
                            f"<<< {Color.green(user_input)}\n¡Felicidades! ¡Ganaste!\nPresione enter para continuar...")

                    guessed = True

                else:
                    print(f"<<< {original_word.verify(user_input)}\n")
                    counter += 1

            if counter == 5:

                if language == "1":
                    input(f"You lost! The word was {Color.red(original_word.word)}\nPress enter to continue...")
                else:
                    print(f"¡Perdiste! La palabra era {Color.red(original_word.word)}")
                    input("Presione enter para continuar...")

    @staticmethod
    def clean() -> None:
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
