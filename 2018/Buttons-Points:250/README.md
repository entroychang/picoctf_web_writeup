# Buttons - Points: 250

1. First, lets go through the website : http://2018shell.picoctf.com:7949/
2. Then, we press the buttons as it said and find there is an interesting video in the end.
3. Next, I check the network in inspect one by one and find that "Button2.php" is a little bit werid cuz the status code is "303 See Other", so I change the method from GET to POST. Then I get the flag.
    You can finish it by Postman or Python.
4. Here is the flag : picoCTF{button_button_whose_got_the_button_3e5652dd}
