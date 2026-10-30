<?php
session_start();
if(!isset($_SESSION['user'])) {
    header("Location: 4.php");
    exit();
}
?>
<h2>Welcome to Dashboard, <?php echo $_SESSION['user']; ?>!</h2>
<a href="6.php">Logout</a>