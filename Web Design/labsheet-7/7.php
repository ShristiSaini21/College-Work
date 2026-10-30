<?php
session_start();
if(isset($_POST['checkout'])) {
    $conn = new mysqli("localhost", "root", "", "bookstore_db");
    $conn->query("INSERT INTO orders (user_id, total_price) VALUES (1, 50.00)");
    unset($_SESSION['cart']);
    echo "Order placed successfully!";
}
?>
<form method="POST">
    <h3>Checkout</h3>
    <input type="text" placeholder="Shipping Address" required><br>
    <button type="submit" name="checkout">Place Order</button>
</form>