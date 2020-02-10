import requests
from bs4 import BeautifulSoup
import json
import pprint
import re
from contextlib import contextmanager
import webbrowser

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
    def __init__(self, name, url):
        self.name = name
        self.url = url

#    def getTitles(self, url):



    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = []

        for link in soup.findAll('a', attrs={'href': re.compile("")}):
            # links.update({re.sub('\s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' ')): (link.get('href') if 'http' in link.get('href') else self.name + link.get('href'))})
                                # delete multiple spaces               replace symbols                replace \n to space     add domain to relative links

            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
            address = link.get('href') if 'http' in link.get('href') else self.name + link.get('href')

            #if 'tut.by' in url:
            #    if len(title) > 2 and '/news/' in address:
            #        links.append({
            #            'title': title,
            #            'url': address
            #        })
            if len(title) > 2:
                links.append({
                    'title': title,
                    'url': address
                })

        list_item = '<li class="list-group-item list-group-item-dark text-left"><a href="{}">{}</a></li>'
        result_list = ""

        for i in range(len(links)):
            result_list += (list_item.format(str(links[i]['url']), str(links[i]['title'])))

        main_page = str("""<!DOCTYPE html><html><head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Home page</title>
              </head>
              <body>
              <main class="container-fluid">
                <div class="row">
                    <section class="col-xl-4 col-12">
                    <h2>{}></h2>
                    <ul class="list-group text-center">
                        {}
                    </ul>
                </div>
              </main>
              </body>
            </html>
            """).format(self.name, result_list)

        index = open('qq.html', 'w')
        agr = re.sub('/s+', ' ', main_page.replace('\n', ' '))

        index.write(agr)
        index.close()

        return re.sub('/s+', ' ', main_page.replace('\n', ' '))





class Write(Source):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = []

        for link in soup.findAll('a', attrs={'href': re.compile("")}):
            # links.update({re.sub('\s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' ')): (link.get('href') if 'http' in link.get('href') else self.name + link.get('href'))})
                                # delete multiple spaces               replace symbols                replace \n to space     add domain to relative links

            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
            address = link.get('href') if 'http' in link.get('href') else self.name + link.get('href')

            #if 'tut.by' in url:
            #    if len(title) > 2 and '/news/' in address:
            #        links.append({
            #            'title': title,
            #            'url': address
            #        })
            if len(title) > 2:
                links.append({
                    'title': title,
                    'url': address
                })



        list_item = """
                <div class="col-xl-4 col-12">
                    <h2>></h2>
                    <ul class="list-group text-center">
                        <li class="list-group-item list-group-item-dark text-left"><a href="{}">{}</a></li>
                </ul>
                </div>
                """
        result_list = ""

        for i in range(len(links)):
            result_list += (list_item.format(str(links[i]['url']), str(links[i]['title'])))

        main_page = str("""<!DOCTYPE html><html><head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Home page</title>
              </head>
              <body>
              <main class="container-fluid">
                <div class="row">
                    <div class="col-xl-4 col-12">
                    <h2>{}></h2>
                    <ul class="list-group text-center">
                        {}
                    </ul>
                    </div>
                </div>
              </main>
              </body>
            </html>
            """).format(self.name, result_list)


        index = open('qq.html', 'a')
        agr = re.sub('/s+', ' ', main_page.replace('\n', ' '))

        index.write(agr)
        index.close()

        return re.sub('/s+', ' ', main_page.replace('\n', ' '))


nPlusOne = Source('Nplus1', 'https://nplus1.ru')
#esquire = Write('esquire', 'https://esquire.ru')
#tut = Write('tut.by', 'https://tut.by')


nPlusOne.getLinks('https://nplus1.ru/')
#esquire.getLinks('https://esquire.ru')
#tut.getLinks('https://tut.by')


#class tutLinks(Source):
#    def getLinks(self, url):
#        page = requests.get(url)
#        soup = BeautifulSoup(page.content, 'html.parser')
#        links = []
#
#        links.append({
#            'name': self.name
#        })
#        for link in soup.findAll('a', attrs={'href': re.compile("")}):
#
#            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
#            address = link.get('href') if 'http' in link.get('href') else self.name + link.get('href')
#
#            if len(title) > 2 and '/news/' in address:
#                links.append({
#                    'title': title,
#                    'url': address
#                })
#        return links
#
#tut = tutLinks('https://tut.by')
# pprint.pprint(tut.getLinks('https://tut.by'))
