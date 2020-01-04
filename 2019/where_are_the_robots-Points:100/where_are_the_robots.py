from requests import *
from bs4 import BeautifulSoup

url = 'https://2019shell1.picoctf.com/problem/21868/robots.txt'
r = get(url)

pos = r.text.find('/')
disallow = ''
while (True):
    txt = r.text[pos]
    disallow += txt
    if (txt == 'l'):
        break

    pos += 1

url = 'https://2019shell1.picoctf.com/problem/21868' + disallow
r = get(url)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('flag').get_text()
print(flag)
