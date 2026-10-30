<?php
session_start();
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$book_id = 1;
$res = $conn->query("SELECT stock FROM books WHERE id = $book_id");
$book = $res->fetch_assoc();

if($book['stock'] > 0) {
    echo "Item added to cart successfully!";
} else {
    echo "Sorry, item out of stock!";
}