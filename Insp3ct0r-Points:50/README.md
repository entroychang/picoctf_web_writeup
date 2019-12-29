# Insp3ct0r - Points: 50

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/61676/
2. Then, check the source code : 
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
        <h1>Inspect Me</h1>
          </header>

          <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">What</button>
          <button class="tablink" onclick="openTab('tababout', this, '#222')">How</button>

          <div id="tabintro" class="tabcontent">
        <h3>What</h3>
        <p>I made a website</p>
          </div>

          <div id="tababout" class="tabcontent">
        <h3>How</h3>
        <p>I used these to make this site: <br/>
          HTML <br/>
          CSS <br/>
          JS (JavaScript)
        </p>
        <!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
          </div>

        </div>

      </body>
    </html>
    ```
    You can see the 1/3 of the flag.
3. So, we can search the whole source code by clicking "customized and control dev tools" and "search" by google chrome.
4. Here is the flag : picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?1638dbe7}
