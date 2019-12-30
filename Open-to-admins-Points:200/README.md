# Open-to-admins - Points: 200

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/37878/
2. Then, we read the discription : 
    "This secure website allows users to access the flag only if they are admin and if the time is exactly 1400." and the hints : "Can cookies help you to get the flag?"
3. So, lets new two cookies named "admin" and "time" : 
    ```
    cookies = {
        'admin' : 'True',
        'time' : '1400'
    }
    ```
    Then, press the "flag" button and get the flag.
4. Here is the flag : picoCTF{0p3n_t0_adm1n5_2e8d3883}
