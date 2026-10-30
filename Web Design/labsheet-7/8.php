<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
if(isset($_POST['add_book'])) {
    $title = $_POST['title'];
    $author = $_POST['author'];
    $price = $_POST['price'];
    $stock = $_POST['stock'];
    $conn->query("INSERT INTO books (title, author, price, stock) VALUES ('$title', '$author', '$price', '$stock')");
}
?>
<h2>Admin Dashboard</h2>
<form method="POST">
    <input type="text" name="title" placeholder="Title" required>
    <input type="text" name="author" placeholder="Author" required>
    <input type="number" step="0.01" name="price" placeholder="Price" required>
    <input type="number" name="stock" placeholder="Stock" required>
    <button type="submit" name="add_book">Add Book</button>
</form>