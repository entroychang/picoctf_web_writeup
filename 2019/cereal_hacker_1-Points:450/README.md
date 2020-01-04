# cereal hacker 1 - Points: 450

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/37889/index.php?file=login
2. Then, we first check sql injection and find that basic boolen injection can't pass the test, so we have to check all weak username and password first. After tones of time, I get a payload : 
    ```
    username : guest
    password : guest
    ```
3. Next, we see that we get nothing in the page, so I turn the file to "admin" https://2019shell1.picoctf.com/problem/37889/index.php?file=admin and we still get nothing.
4. Then, I start to check cookies and find that there is a data named "user_info", so I try to google it how to decode it. In the end, I decode it by base64 and get the payload : 
    ```
    O:11:"permissions":2:{s:8:"username";s:5:"guest";s:8:"password";s:5:"guest";}
    ```
    Now, we have to know the meaning of the payload. 'O' -> Object, 's' -> string
4. After the meaning of it, we have to think of a payload that we can be "admin". Finally, I figure out a payload : 
    ```
    O:11:"permissions":2:{s:8:"username";s:16:"admin' and 1=1 #";s:8:"password";s:1:"1";}
    ```
    So, why this payload? Cuz I don't want to care the password and I am "admin". It's base64 encode : 
    ```     
    TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6MTY6ImFkbWluJyBhbmQgMT0xICMiO3M6ODoicGFzc3dvcmQiO3M6MToiMSI7fQ==
    ```
    Remember to replace the old cookie.
6. Here is the flag : picoCTF{5a1aa7dfd74a9b67bc5844b8245c9d2e}
