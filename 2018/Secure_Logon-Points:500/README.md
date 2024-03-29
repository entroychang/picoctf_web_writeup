# Secure Logon - Points: 500

1. First, lets go through the website : http://2018shell.picoctf.com:56265/
2. Then, I input
    ```
    username : 123
    password : 456
    ```
    And get : 
    ```
    Cookie: {'password': '456', 'username': '123', 'admin': 0}
    ```
3. Next, I check the source code : 
    ```
    from flask import Flask, render_template, request, url_for, redirect, make_response, flash
    import json
    from hashlib import md5
    from base64 import b64decode
    from base64 import b64encode
    from Crypto import Random
    from Crypto.Cipher import AES

    app = Flask(__name__)
    app.secret_key = 'seed removed'
    flag_value = 'flag removed'

    BLOCK_SIZE = 16  # Bytes
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                    chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    @app.route("/")
    def main():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.form['user'] == 'admin':
            message = "I'm sorry the admin password is super secure. You're not getting in that way."
            category = 'danger'
            flash(message, category)
            return render_template('index.html')
        resp = make_response(redirect("/flag"))

        cookie = {}
        cookie['password'] = request.form['password']
        cookie['username'] = request.form['user']
        cookie['admin'] = 0
        print(cookie)
        cookie_data = json.dumps(cookie, sort_keys=True)
        print(cookie_data)
        encrypted = AESCipher(app.secret_key).encrypt(cookie_data)
        print(encrypted)
        resp.set_cookie('cookie', encrypted)
        return resp

    @app.route('/logout')
    def logout():
        resp = make_response(redirect("/"))
        resp.set_cookie('cookie', '', expires=0)
        return resp

    @app.route('/flag', methods=['GET'])
    def flag():
      try:
          encrypted = request.cookies['cookie']
      except KeyError:
          flash("Error: Please log-in again.")
          return redirect(url_for('main'))
      data = AESCipher(app.secret_key).decrypt(encrypted)
      data = json.loads(data)

      try:
         check = data['admin']
      except KeyError:
         check = 0
      if check == 1:
          return render_template('flag.html', value=flag_value)
      flash("Success: You logged in! Not sure you'll be able to see the flag though.", "success")
      return render_template('not-flag.html', cookie=data)

    class AESCipher:
        """
        Usage:
            c = AESCipher('password').encrypt('message')
            m = AESCipher('password').decrypt(c)
        Tested under Python 3 and PyCrypto 2.6.1.
        """

        def __init__(self, key):
            self.key = md5(key.encode('utf8')).hexdigest()

        def encrypt(self, raw):
            raw = pad(raw)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return b64encode(iv + cipher.encrypt(raw))

        def decrypt(self, enc):
            enc = b64decode(enc)
            iv = enc[:16]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(enc[16:])).decode('utf8')

    if __name__ == "__main__":
        app.run()
    ```
    As you can see, "secret_key" and "flag_value" are removed. We know that we have to change "admin" into "1" to get the flag. The keyword is "AES", so I google it and find that there are "CBC" "ECB" "CTR" "OCF" "CFB" ways to encrypt and decrypt. After a long time struggling, I find out that "CBC" is the keywords we need.
4. The attack called Bit Flipping Attack on CBC Mode. You can get more information here : 
https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode
5. Then, I write a script to get the flag. The only thing that you have to do is know how CBC works and you can easily realize what the code mean.
6. Here is the flag : picoCTF{fl1p_4ll_th3_bit3_2efa4bf8}
