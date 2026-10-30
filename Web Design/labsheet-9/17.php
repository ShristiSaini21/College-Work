<?php
if(isset($_POST['login'])) {
    setcookie("user", $_POST['username'], time() + (86400 * 30), "/");
}
$welcome = isset($_COOKIE['user']) ? "Welcome back, " . $_COOKIE['user'] : "Please login.";
?>
<h3><?php echo $welcome; ?></h3>
<form method="POST">
    <input type="text" name="username" placeholder="Username">
    <button type="submit" name="login">Login with Remember Me</button>
</form>