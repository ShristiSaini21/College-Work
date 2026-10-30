<?php
session_start();
$conn = new mysqli("localhost", "root", "", "bookstore_db");

if(isset($_POST['register'])) {
    $user = $_POST['username'];
    $email = $_POST['email'];
    $pass = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $conn->query("INSERT INTO users (username, email, password) VALUES ('$user', '$email', '$pass')");
}

if(isset($_POST['login'])) {
    $email = $_POST['email'];
    $pass = $_POST['password'];
    $res = $conn->query("SELECT * FROM users WHERE email='$email'");
    $row = $res->fetch_assoc();
    if($row && password_verify($pass, $row['password'])) {
        $_SESSION['user'] = $row['username'];
        echo "Login Successful!";
    } else {
        echo "Invalid Credentials!";
    }
}
?>
<form method="POST">
    <h3>Register</h3>
    <input type="text" name="username" placeholder="Username" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit" name="register">Register</button>
</form>
<form method="POST">
    <h3>Login</h3>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit" name="login">Login</button>
</form>