import requests
from bs4 import BeautifulSoup

class rae:
    def search(word):
        url = f'https://dle.rae.es/{word}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            existencia = soup.find_all(True, {"class":["j"]})
            if existencia:
                return True
            else:
                return False
        else:
            raise ConnectionError(f'Error al hacer la solicitud. Código de estado: {response.status_code}')

