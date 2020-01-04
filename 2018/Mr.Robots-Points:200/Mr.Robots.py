from requests import *
from bs4 import BeautifulSoup

url = 'http://2018shell.picoctf.com:60945/robots.txt'
r = get(url)

pos = r.text.find('/')
disallow = ''
while (True):
    txt = r.text[pos]
    disallow += txt
    if (txt == 'l'):
        break

    pos += 1

url = 'http://2018shell.picoctf.com:60945/' + disallow
r = get(url)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('flag').get_text()
print(flag)
