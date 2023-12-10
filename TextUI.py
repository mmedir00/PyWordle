from Words import *
from Color import *
from Rae import *
from EnglishDictionary import *

import os

class TextUI:
    def init():
        userInput = str(input("Welcome to WORDLE!\n1. English\n2. Español\n3. Quit\n>>> "))
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
                    userInput = str(input("\nAttempt " + Color.red(str(counter + 1)) + "\n>>> "))
                elif language == "2":
                    userInput = str(input("\nIntento " + Color.red(str(counter + 1)) + "\n>>> "))

                if (not EnglishDictionary.search(userInput)) and (language == "1"):
                    print("The word doesn't exist")
                elif (not Rae.search(userInput)) and (language == "2"):
                    print("La palabra no existe")

                elif len(userInput) != 5:

                    if language == "1":
                        print("The word must have 5 letters")
                    elif language == "2":
                        print("La palabra debe tener 5 letras")

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
                    input("¡Perdiste! La palabra era " + Color.red(originalWord) + "Presione enter para continuar...")


    def clean():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    
