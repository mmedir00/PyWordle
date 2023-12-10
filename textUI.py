from words import *
from color import *
from raeSearch import *

import os

class textUI:
    def init():
        users = str(input("Welcome to WORDKE!\n1. English\n2. Español\n3. Quit\n>>> "))
        if users in ["3"]:
            exit()
        elif users in ["1", "2"]:
            words = Words(users)
            if users == "1":
                textUI.english(words)
            elif users in ["2"]:
                textUI.espanol(words)

    def espanol(words):
        textUI.clean()
        print("Intente adivinar la palabra secreta!\n5 letras, 5 intentos\n")
        originalWordList = words.getList(words.randomWord())
        counter = 0
        while counter < 5:
            users = str(input("\nIntento " + color.red(str(counter + 1)) + "\n>>> "))
            if rae.search(users) == False:
                print("La palabra no existe")
                continue
            wordList = originalWordList.copy()
            inputList = list(users)
            if len(users) != 5:
                print("La palabra debe tener 5 letras")
            elif inputList == wordList:
                print(f"<<< {color.green(users)}")
                print("¡Felicidades! ¡Ganaste!")
                break
            else:
                print(f"<<< {textUI.verify(inputList, wordList)}\n")
                counter += 1
                
        if counter == 5:
            print("¡Perdiste! La palabra era " + color.red("".join(originalWordList)))


    def english(words):
        pass

    def clean():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    def verify(inputList, wordList):
        string = ""
        for i in range(5):
            if inputList[i] == wordList[i]:
                string += color.green(inputList[i])
                wordList[i] = " "
            elif inputList[i] in wordList:
                string += color.orange(inputList[i])
                wordList[textUI.buscar(wordList, inputList[i])] = " "
            else:
                string += color.grey(inputList[i])
        return string
    
    def buscar(lista, letra):
        for i in range(len(lista)):
            if lista[i] == letra:
                return i
