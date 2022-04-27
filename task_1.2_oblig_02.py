# Libary Overview
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Get HTML and retrive link for images
html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})

# created for the purpose of removing "//" from link
for image in images: 
    x = (image['src']+'\n')
    z = x.strip("//")
    print(z)