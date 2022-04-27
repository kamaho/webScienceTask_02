# Libary Overview
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a', href=True):
    print(link['href'])