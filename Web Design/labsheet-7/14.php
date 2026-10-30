<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$author = "J.K. Rowling";
$stmt = $conn->prepare("SELECT * FROM books WHERE author = ?");
$stmt->bind_param("s", $author);
$stmt->execute();
$result = $stmt->get_result();
while($row = $result->fetch_assoc()) {
    echo $row['title'] . "<br>";
}