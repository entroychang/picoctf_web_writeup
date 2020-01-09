# A Simple Question - Points: 650

1. First, lets go through the website : http://2018shell.picoctf.com:36052/
2. Then, we could find out that there is no hint ... so we have to really guess what is going on.
3. Next, I google "sql injection guessing" and get the useful website : https://sqlzoo.net/hack/16password.htm With this website, we are able to guess the answer with brute force attack by python. Here is my payload : 
    ```
    123' or answer like '{}%
    ```
4. After a long time running, I get the answer "41andsixsixths". However, sqlite3 needs the correct name, which means that some of the charactors might be upper ... So, I brute force attack it by python and finally get the answer "41AndSixSixths" and the flag.
5. Here is the flag : picoCTF{qu3stions_ar3_h4rd_d3850719}
