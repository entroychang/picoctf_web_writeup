# Irish-Name-Repo 1 - Points: 300

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/27383/
2. Then, we find that there is a login page. The first thing I think about is sql injection, so I input : 
    ```
    username : ' or 1=1 /*
    password : 123
    ```
    And I get the flag.
3. Here is the flag : picoCTF{s0m3_SQL_1fe77718}
