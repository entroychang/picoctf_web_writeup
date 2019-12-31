# Irish-Name-Repo 3 - Points: 400

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/32237/
2. Then, we could find a login page. In the begining, I think that it is a sql injection, and it really is. But, the hint is "Seems like the password is encrypted." Maybe the critical keywords like "or" or all words are encrypted, so we have to find out how the website encrypted the words.
3. Now, check the https://2019shell1.picoctf.com/problem/32237/login.php form data after you type a password you like, and you might see the information below : 
    ```
    password: admin' or 1=1 /*
    debug: 0
    ```
    As you can see, the "debug" part is "false", so lets turn the "debug" value into "1" and check the information. You can use Python, Postman or what ever you want.
    ```
    <pre>password: admin' or 1=1 /*
    SQL query: SELECT * FROM admin where password = 'nqzva' be 1=1 /*'
    </pre>
    ```
    So, we know how they do, lets turn the payload into : 
    ```
    password : nqzva' be 1=1 /*
    debug : 1
    ```
    And there is the flag.
4. Here is the flag : picoCTF{3v3n_m0r3_SQL_5c27c4ea}
