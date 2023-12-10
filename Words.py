from Color import *

import random

class Words:
    def __init__(self, language):

        if language == "1":
            self.wordList = ["apple", "table", "chair", "music", "green", "happy", "hello", "water", "watch", "cloud",
                                "river", "beach", "tiger", "bacon", "storm", "chess", "plant", "stone", "grape", "lemon",
                                "pizza", "queen", "laugh", "smile", "clock", "magic", "candy", "frost", "black", "white",
                                "space", "heart", "earth", "robot", "sugar", "honey", "sunny", "wrist", "laser", "dance",
                                "drift", "smoke", "fleet", "swirl", "shine", "spark", "dream", "sweep", "spice", "guide",
                                "ocean", "grind", "crown", "blink", "dream", "frost", "crisp", "charm", "blend", "creek",
                                "flame", "fable", "globe", "lunar", "music", "novel", "piano", "swift", "trend", "vivid",
                                "zebra", "dream", "frost", "scent", "peace", "blend", "creek", "daisy", "drift", "frost",
                                "gloom", "hinge", "jolly", "knots", "mirth", "nudge", "prism", "quiet", "scary", "taste",
                                "usher", "vivid", "waste", "xerox", "yield", "zesty"]
        elif language == "2":
            self.wordList = ['abeja', 'banco', 'casas', 'dobla', 'subir', 'carro', 'grano', 'huevo', 'igual', 'joven',
                            'peral', 'luces', 'madre', 'tabla', 'aureo', 'papel', 'queso', 'radio', 'silla', 'audio',
                            'pulpo', 'barco', 'clima', 'ducha', 'casco', 'globo', 'hojas', 'islas', 'jugar', 'lugar', 
                            'llama', 'mundo', 'naran', 'sonda', 'potro', 'verde', 'perro', 'cable', 'amigo', 'botas', 
                            'rueda', 'danza', 'cuero', 'flota', 'giras', 'hongo', 'juego', 'lince', 'mambo', 'nunca', 
                            'oasis', 'pasta', 'ronda', 'tango', 'hueso', 'volar', 'setas', 'bello', 'crudo', 'demon', 
                            'etnia', 'fuego', 'gusto', 'monja', 'ileso', 'huida', 'leche', 'noble', 'oruga', 'pista', 
                            'roble', 'salsa', 'terno', 'abraz', 'buche', 'cuota', 'delta', 'ejejo', 'fruta', 
                            'gafas', 'herir', 'izote', 'jorco', 'mujer', 'nopal', 'ojear', 'meter', 'sable', 'tinta', 
                            'umbra', 'parce', 'bache', 'metro', 'reloj', 'medro', 'cabal', 'monte', 'lente', 'azote', 
                            'ceibo', 'fosil', 'nacer', 'aleta', 'monta', 'elevo', 'cerco', 'alojo', 'maple', 'merlo', 
                            'broma', 'limar', 'carpa', 'temor', 'carne', 'pelar', 'miedo', 'selva', 'aroma', 'besar', 
                            'anexo', 'risco', 'hedor', 'craso', 'foral', 'sueco', 'hogar', 'sogas', 'balsa', 'hablo', 
                            'tomar', 'barro', 'yogur', 'sordo', 'horno', 'regio', 'huele', 'naveo', 'roper', 'falsa', 
                            'minar', 'capaz', 'brote', 'marco', 'virus', 'coser', 'manar', 'vario', 'zafio', 'pieza', 
                            'tiara', 'matiz', 'trago', 'tirar', 'tesor', 'fieza', 'larva', 'samba', 'vuela', "llave"
                            'latir', 'torpe', 'ruedo', 'timar', 'tumba', 'pilar', 'saber', 'desde', 'jorar', 'oliva', 
                            'quedo', 'cinta', 'trono', 'pared', 'largo', 'sutil', 'salto', 'helio', 'estor', 'bicho', 
                            'fumar', 'plomo', 'ducho', 'siete', 'cenar', 'letra', 'doble']

    def randomWord(self):
        return random.choice(self.wordList)
    
    def search(self, letter, word):
        for i in range(len(word)):
            if letter == word[i]:
                return i
            
    def verify(self, inputWord, word):
        inputList = list(inputWord)
        wordList = list(word)
        string = ["","","","",""]
        greenList = wordList
        for i in range(5):
            if inputList[i] == greenList[i]:
                string[i] = Color.green(inputList[i])
                greenList[i] = " "
        for i in range(5):
            if inputList[i] in greenList and string[i] != Color.green(inputList[i]):
                string[i] = Color.yellow(inputList[i])
                greenList[self.search(inputList[i], greenList)] = " "
        for i in range(5):
            if string[i] == "":
                string[i] = Color.grey(inputList[i])
        return "".join(string)