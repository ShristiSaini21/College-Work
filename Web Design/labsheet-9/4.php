<?php
session_start();
require_once '2.php';
if(isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $user = $stmt->get_result()->fetch_assoc();
    
    if($user && password_verify($password, $user['password'])) {
        $_SESSION['user'] = $user['username'];
        header("Location: 5.php");
    } else { echo "Invalid Credentials!"; }
}
?>
<form method="POST">
    <input type="email" name="email" placeholder="Email" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <button type="submit" name="login">Login</button>
</form>