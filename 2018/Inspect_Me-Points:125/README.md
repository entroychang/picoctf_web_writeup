# Inspect Me - Points: 125

1. First, lets go through the website : http://2018shell.picoctf.com:28831/
2. Then, we check the source code : 
    ```
    <!doctype html>
    <html>
      <head>
        <title>My First Website :)</title>
        <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="mycss.css">
        <script type="application/javascript" src="myjs.js"></script>
      </head>

      <body>
        <div class="container">
          <header>
        <h1>My First Website</h1>
          </header>

          <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">Intro</button>
          <button class="tablink" onclick="openTab('tababout', this, '#222')">About</button>

          <div id="tabintro" class="tabcontent">
        <h3>Intro</h3>
        <p>This is my first website!</p>
          </div>

          <div id="tababout" class="tabcontent">
        <h3>About</h3>
        <p>These are the web skills I've been practicing: <br/>
          HTML <br/>
          CSS <br/>
          JS (JavaScript)
        </p>
        <!-- I learned HTML! Here's part 1/3 of the flag: picoCTF{ur_4_real_1nspe -->
          </div>

        </div>

      </body>
    </html>
    ```
    You can see the 1/3 of the flag.
3. So, we can search the whole source code by clicking "customized and control dev tools" and "search" by google chrome.
4. Here is the flag : picoCTF{ur_4_real_1nspect0r_g4dget_b4887011}
