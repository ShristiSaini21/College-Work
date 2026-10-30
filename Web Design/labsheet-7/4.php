<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$id = $_GET['id'];
$stmt = $conn->prepare("SELECT * FROM books WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$book = $stmt->get_result()->fetch_assoc();
?>
<!DOCTYPE html>
<html>
<head><title>Book Details</title></head>
<body>
    <h1><?php echo $book['title']; ?></h1>
    <p>Author: <?php echo $book['author']; ?></p>
    <p>Price: $<?php echo $book['price']; ?></p>
    <p>Stock: <?php echo $book['stock']; ?></p>
    <button>Add to Cart</button>
</body>
</html>