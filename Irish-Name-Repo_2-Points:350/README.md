# Irish-Name-Repo 2 - Points: 350

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/7411/
2. Then, we find the login page and try sql injection and find that it will be detected.
3. So, I look up hints "The password is being filtered." such as "or" "union" "select". 
4. Then I input the payload : 
    ```
    username : admin' --
    password : 123
    ```
    And I get the flag.
5. Here is the flag : picoCTF{m0R3_SQL_plz_c1c3dff7}
