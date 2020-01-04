# Logon - Points: 150

1. First, lets go through the website : http://2018shell.picoctf.com:6153/
2. After seeing the login page, I first tried sql injection : 
    ```
    username = ' or 1=1 /*
    password = 123
    ```
    I get nothing.
3. Then, I check cookies and find that there is an interesting parameter "admin" with "False". Next, I tried to change it to "True" and get the flag.
4. Here is the flag : picoCTF{l0g1ns_ar3nt_r34l_82e795f4}
