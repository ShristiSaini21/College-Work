<?php
session_start();
require_once '2.php';
$conn->begin_transaction();
try {
    $conn->query("INSERT INTO orders (user_id, total_amount) VALUES (1, 150.00)");
    $conn->commit();
    echo "Order placed successfully via Transaction!";
} catch (mysqli_sql_exception $exception) {
    $conn->rollback();
    echo "Transaction failed: " . $exception->getMessage();
}
?>