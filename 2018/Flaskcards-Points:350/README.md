# Flaskcards - Points: 350

1. First, lets go through the website : http://2018shell.picoctf.com:17991/
2. Then, we register and login. Next, I struggle for a long time after I google "flask", I find the answer.
3. "Flask" is a backend of Python, so the only way we can input is "Create Card". Here is the payload : 
    ```
    {{config}}
    ```
    After you input it and go through "List Cards", you can see the flag. By the way, I don't know what admin does in this challenge.
4. Here is the flag : picoCTF{secret_keys_to_the_kingdom_45e7608d}
