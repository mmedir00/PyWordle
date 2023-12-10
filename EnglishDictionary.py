import requests
from bs4 import BeautifulSoup

class EnglishDictionary:
    def search(word):
        url = f'https://www.dictionary.com/browse/{word}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            existencia = soup.find_all(True, {"class":["r9VbteV96t3N9RUC5Rkg"]})
            if existencia:
                return True
            else:
                return False
        elif response.status_code == 404:
            return False
        else:
            raise ConnectionError(f'Error al hacer la solicitud. Código de estado: {response.status_code}')