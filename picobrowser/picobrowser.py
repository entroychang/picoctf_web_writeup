from requests import *
from bs4 import BeautifulSoup

url = 'https://2019shell1.picoctf.com/problem/49789/flag'
headers = {
    'User-Agent' : 'picobrowser'
}
r = get(url , headers=headers)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
