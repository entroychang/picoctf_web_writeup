# No Login - Points: 200

1. First, lets go through the website : http://2018shell.picoctf.com:10573/
2. Then, we read the discription "Looks like someone started making a website but never got around to making a login, but I heard there was a flag if you were the admin." and the hints "What is it actually looking for in the cookie?"
3. So, lets create a cookie named "admin" and the value is "True".
    ```
    cookies = {
        'admin' : 'True'
    }
    ```
    Then, press the "flag" button to get the flag.
4. Here is the flag : picoCTF{n0l0g0n_n0_pr0bl3m_ed714e0e}
