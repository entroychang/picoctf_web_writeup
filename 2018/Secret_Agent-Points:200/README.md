# Secret Agent - Points: 200

1. First, lets go through the website : http://2018shell.picoctf.com:3827/
2. Then, we press flag and see "You're not google! Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
3. So, I need to be "google" in order to get the flag. I google "google agent" and get the code from "Googlebot" : 
    ```
    Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
    ```
    Then, I change the user agent into this and get the flag.
    You can use Postman or Python to reach the goal.
4. Here is the flag : picoCTF{s3cr3t_ag3nt_m4n_12387c22}
