<?php
// Write a PHP script implementing transaction management (`beginTransaction()`, `commit()`, `rollBack()`) in MySQL PDO for secure multi-table operations.[cite: 13]
$host = 'localhost';
$db   = 'college_db';
$user = 'root';
$pass = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Start transaction
    $pdo->beginTransaction();

    // Query 1
    $pdo->exec("INSERT INTO students (name, email) VALUES ('Aman Verma', 'aman@example.com')");
    
    // Query 2 (Simulated multi-table operation or audit log)
    // $pdo->exec("INSERT INTO logs ...");

    // Commit transaction if all queries succeed
    $pdo->commit();
    echo "Transaction committed successfully!";
} catch (Exception $e) {
    // Rollback transaction if any error occurs
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    echo "Transaction failed and rolled back: " . $e->getMessage();
}
?>