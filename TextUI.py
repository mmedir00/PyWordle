from Words import *
from Color import *
from WordValidator import *

import os

class TextUI:
    def init():
        TextUI.clean()
        print(Color.purple("--WELCOME TO PYWORDLE!--") + "\nWebScrapping on " + Color.red("dle.rae.es") + " and "  + Color.blue("www.dictionary.com") + " for word validation\n" + Color.grey("by @MarcMeRu\n"))
        userInput = str(input("1. English\n2. Español\n3. Quit\n>>> "))
        if userInput in ["3"]:
            exit()
        elif userInput in ["1", "2"]:
            words = Words(userInput)
            TextUI.gameLoop(words, userInput)

    def gameLoop(words, language):
        while True:
            TextUI.clean()
            if language == "1":
                print("Try to guess the secret word!\n5 letters, 5 attempts\n")
            elif language == "2":
                print("Intente adivinar la palabra secreta!\n5 letras, 5 intentos\n")
            originalWord = words.randomWord()
            counter = 0
            guessed = False
            while counter < 5 and not guessed:
                
                if language == "1":
                    userInput = str(input("\nAttempt " + Color.blue(str(counter + 1)) + "\n>>> "))
                elif language == "2":
                    userInput = str(input("\nIntento " + Color.blue(str(counter + 1)) + "\n>>> "))
                
                if not WordValidator.validateLength(userInput):
                    if language == "1":
                        print(Color.red("The word must have 5 letters"))
                    elif language == "2":
                        print(Color.red("La palabra debe tener 5 letras"))
                
                elif not WordValidator.validateDictionary(userInput, language):
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
                    print(f"<<< {words.verify(userInput, originalWord)}\n")
                    counter += 1
                    
            if counter == 5:

                if language == "1":
                    input(f"You lost! The word was {Color.red(originalWord)}\nPress enter to continue...")
                elif language == "2":
                    input(f"¡Perdiste! La palabra era {Color.red(originalWord)}\nPresione enter para continuar...")


    def clean():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    
