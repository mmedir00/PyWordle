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
            self.wordList = ["abeja", "banco", "casas", "dobla", "subir", "carro", "grano", "huevo", "igual", "joven",
                                "peral", "luces", "madre", "tabla", "aureo", "papel", "queso", "radio", "silla", "audio",
                                "pulpo", "barco", "clima", "ducha", "casco", "globo", "hojas", "islas", "jugar", "lugar",
                                "llama", "mundo", "naran", "sonda", "potro", "queso", "verde", "silla", "perro", "cable",
                                "amigo", "botas", "rueda", "danza", "cuero", "flota", "giras", "hongo", "juego", "lince",
                                "mambo", "nunca", "oasis", "pasta", "queso", "ronda", "silla", "tango", "hueso", "volar",
                                "setas", "bello", "crudo", "demon", "etnia", "fuego", "gusto", "monja", "ileso", "huida",
                                "leche", "mundo", "noble", "oruga", "pista", "queso", "roble", "salsa", "terno", "uvita",
                                "abraz", "buche", "cuota", "delta", "ejejo", "fruta", "gafas", "herir", "izote", "jorco",
                                "llama", "mujer", "nopal", "ojear", "papel", "queso", "meter", "sable", "tinta", "umbra", 
                                "monja"]

    def randomWord(self):
        return random.choice(self.wordList)
    
    def getList(self, word):
        return list(word)

