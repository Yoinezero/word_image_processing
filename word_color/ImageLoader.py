import requests
from bs4 import BeautifulSoup as BSHTML
import os


class ImageLoader:
    def __init__(self, what_to_search: str):
        self.__WEBSITE = 'https://www.google.com/search?'
        self.__HEADERS = {
            'q': what_to_search,
            'hl': 'en',
            'tbm': 'isch',
            'source': 'python',
            'biw': '882',
            'bih': '731',
            'oq': what_to_search,
            'sclient': 'img',
            'uact': '5',
        }
        self.what_to_search = what_to_search
        self.__page = requests.get(self.__WEBSITE, self.__HEADERS)
        os.mkdir('Downloads')
        os.chdir('Downloads')
        self.files = []

    def download(self):
        soup = BSHTML(self.__page.content, 'html.parser')
        images = [image['src'] for image in soup.find_all('img')]
        for i, image in enumerate(images, 0):
            if i == 6:
                break
            if image.startswith('http'):
                self.files.append(f"Downloads/{self.what_to_search}_{i}.png")
                file = open(f"{self.what_to_search}_{i}.png", "wb")
                file.write(requests.get(image).content)
                file.close()
        os.chdir('..')


if __name__ == '__main__':
    print('This module can be used only as module')
