import requests
from bs4 import BeautifulSoup
import json
import pprint
import re



class Article:
    def __init__(self, name):
        self.name = name

    def getArticleStuff(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find('div', class_='body')
        return content

poteplenie = Article('n+1 article')

# print(poteplenie.getArticleStuff('https://nplus1.ru/news/2020/01/29/warm-arctic'))





class Source:
    def __init__(self, name):
        self.name = name

#    def getTitles(self, url):
#        page = requests.get(url)
#        soup = BeautifulSoup(page.content, 'html.parser')
#        titleByClass = soup.findAll('h3')
#        result = {}
#        for i in range(1, len(titleByClass)):
#            # print(titleByClass[i].text)
#            # print(linksByClass[i])
#            result[f"{i} article"] = titleByClass[i].text
#            # result[f"url {i}"] = titleByClass[i]
#            # result[f"url {i}"] = titleByClass[i]
#            return result

    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = {}
        all_a = soup.findAll('main', attrs={'href': re.compile("")})
        for link in soup.findAll('a', attrs={'href': re.compile("")}):
            links.update({(link.text) : 'https://nplus1.ru/' + link.get('href')})
            # links.append(link.get('href'))
            # links.append(link.text)
        headers = soup.findAll('h3')
        return links

nPlusOne = Source('nplus1.ru')

# print(nPlusOne.name)
# pprint.pprint(nPlusOne.getTitles('https://nplus1.ru/'))

pprint.pprint(nPlusOne.getLinks('https://nplus1.ru/'))
