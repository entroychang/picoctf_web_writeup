# logon - Points: 100
1. First, lets go through the website : https://2019shell1.picoctf.com/problem/32270/flag
2. After seeing the login page, I first tried sql injection : 
    ```
    username = ' or 1=1 /*
    password = 123
    ```
    I get nothing.
3. Then, I check cookies and find that there is an interesting parameter "admin" with "False". Next, I tried to change it to "True" and get the flag.
4. Here is the flag : picoCTF{th3_c0nsp1r4cy_l1v3s_a03e3590}
