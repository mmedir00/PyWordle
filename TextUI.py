import Color
from Game import *


class TextUI:
    def __init__(self) -> None:
        clean()
        self.language = 0
        self.texts = {
            "Language": {0: Color.purple("Select the language. // Selecciona el Idioma.") + "\n1. English\n2. Español\n3. Quit\n>>>"},

            "GameMode": {
                1: Color.purple("Select a game mode:") + "\n1-Common game.\n2-Difficult game.\n3-Hardcore game.\n4-Endless game.\n5-Go back.\n>>>",
                2: Color.purple("Selecciona un modo de juego:") + "\n1-Normal.\n2-Dificil.\n3-Hardcore.\n4-Infinito.\n5-Volver.\n>>>"},

            "GameOver": {
                1: Color.red("Game Over.") + " You won {0}/{1} times.",
                2: Color.red("Perdiste.") + " Ganaste {0}/{1} veces."},

            "Won": {
                1: Color.green("You won") + " {0} times in a row.",
                2: Color.green("Ganaste" + " {0} times in a row")},

            "Continue": {
                1: Color.purple("Continue game? Press enter to continue, type exit to stop.") + "\n>>>",
                2: Color.purple("¿Continuar el juego? presiona Enter para continuar, escribe exit para salir.") + "\n>>>"},

            "Exit": {
                3: "Exiting game.//Saliendo del juego."}
        }
        print(
            "{0}\nWebScrapping on {1} and {2} for word validation\n{3}".format(Color.purple("--WELCOME TO PYWORDLE!--"),
                                                                               Color.red(
                                                                                   "dle.rae.es"),
                                                                               Color.blue("www.dictionary.com"),
                                                                               Color.grey(
                                                                                   "by @MarcMeRu\n")))
        self.menu_language()

    def menu_language(self) -> None:
        while self.language not in range(1, 4):
            self.language = int(input(self.texts["Language"][self.language]))

        if self.language in [1, 2]:
            self.menu_game()
        else:
            print(self.texts["Exit"][self.language])
            exit()

    def menu_game(self) -> None:
        select = 0
        while select not in range(1, 6):
            select = int(input(self.texts["GameMode"][self.language]))

        if select == 1:
            self.common_game()
        elif select == 2:
            self.advanced_game(5)
        elif select == 3:
            self.advanced_game(5)
        elif select == 4:
            self.nonstop_game()
        else:
            self.menu_language()

    def common_game(self) -> None:
        game = Game(self.language)
        game.game_loop()
        self.menu_game()

    def advanced_game(self, games: int) -> None:
        count = 0;
        loose = False
        while count < games and not loose:
            game = Game(self.language)
            loose = not game.game_loop()
            count += 1
        if loose:
            print(self.texts["GameOver"][self.language].format(count + 1, games))
        else:
            print(self.texts["Won"][self.language].format(games))
        self.menu_game()

    def nonstop_game(self) -> None:
        count = 0
        win_count = 0
        loop = True
        while loop:
            game = Game(self.language)
            if game.game_loop():
                win_count += 1
            count += 1
            if str(input(self.texts["Continue"][self.language])).lower() in ["exit", "e"]:
                print(self.texts["Game over."][self.language].format(count, win_count))
                self.menu_language()
