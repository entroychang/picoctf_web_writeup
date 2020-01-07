# Help Me Reset 2 - Points: 600 

1. First, lets go through the website : http://2018shell.picoctf.com:45948/
2. Then, we check the hint "Try looking past the typical vulnerabilities. Think about possible programming mistakes.", so sql injection may not be the correct answer of this challenge.
3. Since I have no idea, I use WFUZZ to scan the website and find an interesting file "profile". Then, I get the flag. Here is the payload : 
    ```
    wfuzz -w wfuzz/wordlist/general/common.txt http://2018shell.picoctf.com:45948/FUZZ | grep 200
    ```
4. Here is the flag : picoCTF{i_thought_i_could_remember_those_34745314}
