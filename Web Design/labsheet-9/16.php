<?php
$userInput = "<script>alert('XSS Attack');</script>";
echo "Raw: " . $userInput . "<br>";
echo "Protected: " . htmlspecialchars($userInput, ENT_QUOTES, 'UTF-8');
?>