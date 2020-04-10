#use requests and beautifulsoup is print to screen the content of the article

import requests
from bs4 import BeautifulSoup
import parser

url = 'http://www.practicepython.org/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')

# print(soup.find_all('article'))

for link in soup.find_all('a'):
    print(link.get('href'))