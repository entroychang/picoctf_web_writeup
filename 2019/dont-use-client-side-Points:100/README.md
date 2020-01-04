# dont-use-client-side - Points: 100

1. First, lets go through this website : https://2019shell1.picoctf.com/problem/21888/
2. Then we view the source code of the website : 
    ```
      function verify() {
        checkpass = document.getElementById("pass").value;
        split = 4;
        if (checkpass.substring(0, split) == 'pico') {
          if (checkpass.substring(split*6, split*7) == '6a8e') {
            if (checkpass.substring(split, split*2) == 'CTF{') {
             if (checkpass.substring(split*4, split*5) == 'ts_p') {
              if (checkpass.substring(split*3, split*4) == 'lien') {
                if (checkpass.substring(split*5, split*6) == 'lz_5') {
                  if (checkpass.substring(split*2, split*3) == 'no_c') {
                    if (checkpass.substring(split*7, split*8) == 'b}') {
                      alert("Password Verified")
                      }
                    }
                  }

                }
              }
            }
          }
        }
        else {
          alert("Incorrect password");
        }

      }
    ```
    So, we just need to piece it back.
3. Here is the flag : picoCTF{no_clients_plz_56a8eb}
