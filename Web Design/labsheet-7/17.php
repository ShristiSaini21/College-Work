<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
if(isset($_GET['wishlist'])) {
    $conn->query("INSERT INTO wishlist (user_id, book_id) VALUES (1, 2)");
    echo "Added to wishlist!";
}
?>
<a href="?wishlist=true">Add to Wishlist ❤️</a>