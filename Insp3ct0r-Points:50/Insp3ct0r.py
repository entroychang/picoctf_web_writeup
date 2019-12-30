from requests import *

def find_flag(text):
    pos = r.text.find('flag')
    count = 0
    while (True):
        txt = r.text[pos]
        if (count > 5 and txt == ' '):
            break
        if (count > 5):
            print(txt , end='')
        count += 1
        pos += 1

url = 'https://2019shell1.picoctf.com/problem/61676/'
r = get(url)
find_flag(r.text)

url = 'https://2019shell1.picoctf.com/problem/61676/mycss.css'
r = get(url)
find_flag(r.text)

url = 'https://2019shell1.picoctf.com/problem/61676/myjs.js'
r = get(url)
find_flag(r.text)
print()
