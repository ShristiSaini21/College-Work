<?php
// Vulnerable Query Example (Demonstration)
// $sql = "SELECT * FROM users WHERE username = '$userInput'";

// Secure Prepared Statement Version
require_once '2.php';
$userInput = "admin";
$stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
$stmt->bind_param("s", $userInput);
$stmt->execute();
$result = $stmt->get_result();
echo "Secure query executed successfully.";
?>