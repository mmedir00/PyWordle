from EnglishDictionary import *
from Rae import *

class WordValidator():
    def validateLength(word):
        if len(word) == 5:
            return True
        else: 
            return False
    
    def validateDictionary(word, language):
        validated = False

        if language == "1":
            validated = EnglishDictionary.search(word)
        elif language == "2":
            validated = Rae.search(word)

        return validated