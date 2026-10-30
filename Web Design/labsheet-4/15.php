<?php
// Write a PHP script demonstrating session management (`session_start()`, `$_SESSION`) to maintain user login state across multiple pages.[cite: 13]
session_start();

// Simulating login state assignment
$_SESSION['username'] = "Suhani";
$_SESSION['role'] = "Administrator";

echo "Session started and user data saved!<br>";
echo "Logged in user: " . $_SESSION['username'] . "<br>";
echo "Role: " . $_SESSION['role'] . "<br>";
echo '<a href="logout.php">Logout (Destroy Session)</a>';
?>