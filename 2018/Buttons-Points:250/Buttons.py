from requests import *

url = 'http://2018shell.picoctf.com:7949/button2.php'
headers = {
    'Host' : '2018shell.picoctf.com:7949',
    'Referer' : 'http://2018shell.picoctf.com:7949/button1.php'
}
r = post(url)
print(r.text)