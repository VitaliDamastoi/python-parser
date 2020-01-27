import requests
from bs4 import BeautifulSoup
import json
import pprint
import re

class Source:
    def __init__(self, name):
        self.name = name

    def getTitles(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        titleByClass = soup.findAll('h3')
        linksByClass = soup.findAll(class_='title', href=True)
        result = {}
        for i in range(1, len(titleByClass)):
            # print(titleByClass[i].text)
            # print(linksByClass[i])
            result[f"{i} article"] = titleByClass[i].text
            # result[f"url {i}"] = titleByClass[i]

            # result[f"url {i}"] = titleByClass[i]
        return result


nPlusOne = Source('nplus1.ru')

# print(nPlusOne.name)
pprint.pprint(nPlusOne.getTitles('https://nplus1.ru/'))

# pprint.pprint(getTitles('https://esquire.ru/'))
