<?php
// Install and connect to the MySQL database server via command line or graphical interface (e.g., phpMyAdmin), creating a new database named `college_db`.[cite: 13]
/*
  MySQL Command to create database:
  CREATE DATABASE college_db;
*/
$servername = "localhost";
$username = "root";
$password = "";

try {
    $conn = new PDO("mysql:host=$servername", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "CREATE DATABASE IF NOT EXISTS college_db";
    $conn->exec($sql);
    echo "Database 'college_db' created successfully or already exists.";
} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}
?>