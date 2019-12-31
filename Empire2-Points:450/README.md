# Empire2 - Points: 450

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/39830/
2. Then, we should find out that it is as same as "Empire1" but after I input the payload in "Add A Todo", I get nothing.
    ```
    payload : '||(select sql from sqlite_master)||'
    ```
    So, I think that there must be anothor way to solve it.
3. Then, I check the cookies and find out a session there. The only thing I do is google "session decode" and find out such as "php session decode" "base64 session decode" and "flask session decode". I tried one by one and finally I success with flask session decode.
    ```
    {
        "_fresh": false,
        "_id": "82d244a4d9273faeb1175d440608b3e34e5aa06f8499a55ea47868df4b8e968494df7a63f5d3030cd021e7ec6313108c4c98dc8fbed5a2bfb55e37b17e8c0968",
        "csrf_token": "12cc51abc8f40927846d95461d76235328d3100d",
        "dark_secret": "picoCTF{its_a_me_your_flag3f43252e}",
        "user_id": "3"
    }
    ```
4. Here is the flag : picoCTF{its_a_me_your_flag3f43252e}
