import random
from Color import *


class Word:
    def __init__(self, language: int) -> None:
        self.word_list = {
            1: ["apple", "table", "chair", "music", "green", "happy", "hello", "water", "watch", "cloud",
                "river", "beach", "tiger", "bacon", "storm", "chess", "plant", "stone", "grape", "lemon",
                "pizza", "queen", "laugh", "smile", "clock", "magic", "candy", "frost", "black", "white",
                "space", "heart", "earth", "robot", "sugar", "honey", "sunny", "wrist", "laser", "dance",
                "drift", "smoke", "fleet", "swirl", "shine", "spark", "dream", "sweep", "spice", "guide",
                "ocean", "grind", "crown", "blink", "dream", "frost", "crisp", "charm", "blend", "creek",
                "flame", "fable", "globe", "lunar", "music", "novel", "piano", "swift", "trend", "vivid",
                "zebra", "dream", "frost", "scent", "peace", "blend", "creek", "daisy", "drift", "frost",
                "gloom", "hinge", "jolly", "knots", "mirth", "nudge", "prism", "quiet", "scary", "taste",
                "usher", "vivid", "waste", "xerox", "yield", "zesty"],

            2: ['abeja', 'banco', 'casas', 'dobla', 'subir', 'carro', 'grano', 'huevo', 'igual', 'joven',
                'peral', 'luces', 'madre', 'tabla', 'aureo', 'papel', 'queso', 'radio', 'silla', 'audio',
                'pulpo', 'barco', 'clima', 'ducha', 'casco', 'globo', 'hojas', 'islas', 'jugar', 'lugar',
                'llama', 'mundo', 'naran', 'sonda', 'potro', 'verde', 'perro', 'cable', 'amigo', 'botas',
                'rueda', 'danza', 'cuero', 'flota', 'giras', 'hongo', 'juego', 'lince', 'mambo', 'nunca',
                'oasis', 'pasta', 'ronda', 'tango', 'hueso', 'volar', 'setas', 'bello', 'crudo', 'dejar',
                'etnia', 'fuego', 'gusto', 'monja', 'ileso', 'huida', 'leche', 'noble', 'oruga', 'pista',
                'roble', 'salsa', 'terno', 'abraz', 'buche', 'cuota', 'delta', 'ejejo', 'fruta', 'gafas',
                'herir', 'izote', 'jorco', 'mujer', 'nopal', 'ojear', 'meter', 'sable', 'tinta', 'letra',
                'umbra', 'parce', 'bache', 'metro', 'reloj', 'medro', 'cabal', 'monte', 'lente', 'azote',
                'ceibo', 'fosil', 'nacer', 'aleta', 'manta', 'elevo', 'cerco', 'alojo', 'maple', 'merlo',
                'broma', 'limar', 'carpa', 'temor', 'carne', 'pelar', 'miedo', 'selva', 'aroma', 'besar',
                'anexo', 'risco', 'hedor', 'craso', 'foral', 'sueco', 'hogar', 'sogas', 'balsa', 'hablo',
                'tomar', 'barro', 'yogur', 'sordo', 'horno', 'regio', 'huele', 'naveo', 'roper', 'falsa',
                'minar', 'capaz', 'brote', 'marco', 'virus', 'coser', 'manar', 'vario', 'zafio', 'pieza',
                'tiara', 'matiz', 'trago', 'tirar', 'tesor', 'fieza', 'larva', 'samba', 'vuela', "llave",
                'torpe', 'ruedo', 'timar', 'tumba', 'pilar', 'saber', 'desde', 'jorar', 'oliva', 'latir',
                'quedo', 'cinta', 'trono', 'pared', 'largo', 'sutil', 'salto', 'helio', 'estor', 'bicho',
                'fumar', 'plomo', 'ducho', 'siete', 'cenar', 'doble', 'texto']}
        self.word = self.random_word(language)

    def __eq__(self, value: str) -> bool:
        return self.word == value.lower()

    def __str__(self):
        return self.word

    def random_word(self, language: int) -> str:
        return random.choice(self.word_list[language])

    @staticmethod
    def search(letter: str, word: [str]) -> int:
        for i in range(len(word)):
            if letter == word[i]:
                return i

    def verify(self, input_word: str) -> str:
        input_list = list(input_word)
        word_list = list(self.word)
        string = ["", "", "", "", ""]
        green_list = word_list

        for i in range(5):
            if input_list[i] == green_list[i]:
                string[i] = Color.green(input_list[i])
                green_list[i] = " "

        for i in range(5):
            if input_list[i] in green_list and string[i] != Color.green(input_list[i]):
                string[i] = Color.yellow(input_list[i])
                green_list[self.search(input_list[i], green_list)] = " "

        for i in range(5):
            if string[i] == "":
                string[i] = Color.grey(input_list[i])

        return "".join(string)
