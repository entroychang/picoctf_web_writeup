from requests import *
from bs4 import BeautifulSoup

url = 'http://2018shell.picoctf.com:3827/flag'
headers = {
    'User-Agent' : 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}
r = get(url , headers=headers)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
