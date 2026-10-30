<?php
// Write a PHP script utilizing `password_hash()` and `password_verify()` to securely store and authenticate hashed user passwords in MySQL.[cite: 13]
$plainPassword = "SecurePassword123";

// Hash password for database storage
$hashedPassword = password_hash($plainPassword, PASSWORD_DEFAULT);
echo "Hashed Password for storage: " . $hashedPassword . "<br><br>";

// Verify user login input against stored hash
$loginInput = "SecurePassword123";
if (password_verify($loginInput, $hashedPassword)) {
    echo "Password Verification Successful! Authentication granted.";
} else {
    echo "Password Verification Failed! Incorrect password.";
}
?>