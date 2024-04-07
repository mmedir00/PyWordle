from Words import *
from WordValidator import *
import os

class TextUI:
    def __init__(self)-> None:
        self.clean()
        print(Color.purple("--WELCOME TO PYWORDLE!--") + "\nWebScrapping on " + Color.red("dle.rae.es") + " and "  + Color.blue("www.dictionary.com") + " for word validation\n" + Color.grey("by @MarcMeRu\n"))
        userInput = str(input("1. English\n2. Español\n3. Quit\n>>> "))
        if userInput in ["3"]:
            exit()
        elif userInput in ["1", "2"]:
            words = Word(userInput)
            self.game_loop(words, userInput)

    def game_loop(self, words:Word, language:int)-> None:
        while True:
            originalWord = Word(language)
            validator = Word_validator(language)
            counter = 0
            guessed = False

            self.clean()
            if language == "1":
                print("Try to guess the secret word!\n5 letters, 5 attempts\n")
            elif language == "2":
                print("Intente adivinar la palabra secreta!\n5 letras, 5 intentos\n")

            while counter < 5 and not guessed:
                
                if language == "1":
                    userInput = str(input("\nAttempt " + Color.blue(str(counter + 1)) + "\n>>> "))
                elif language == "2":
                    userInput = str(input("\nIntento " + Color.blue(str(counter + 1)) + "\n>>> "))
                
                if not validator.validate_length(userInput):
                    if language == "1":
                        print(Color.red("The word must have 5 letters"))
                    elif language == "2":
                        print(Color.red("La palabra debe tener 5 letras"))
                
                elif not validator.validate_dictionary(userInput):
                    if language == "1":
                        print(Color.red("The word doesn't exist in the dictionary."))
                    elif language == "2":
                        print(Color.red("La palabra no existe en el diccionario."))

                elif userInput == originalWord:
                    if language == "1":
                        input(f"<<< {Color.green(userInput)}\nCongratulations! You won!\nPress enter to continue...")
                    elif language == "2":
                        input(f"<<< {Color.green(userInput)}\n¡Felicidades! ¡Ganaste!\nPresione enter para continuar...")

                    guessed = True

                else:
                    print(f"<<< {originalWord.verify(userInput)}\n")
                    counter += 1
                    
            if counter == 5:

                if language == "1":
                    input(f"You lost! The word was {Color.red(originalWord.word)}\nPress enter to continue...")
                elif language == "2":
                    input(f"¡Perdiste! La palabra era {Color.red(originalWord.word)}\nPresione enter para continuar...")


    def clean(self)-> None:
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    
