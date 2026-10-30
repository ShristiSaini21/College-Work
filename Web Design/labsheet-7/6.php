<?php
session_start();
if(!isset($_SESSION['cart'])) { $_SESSION['cart'] = []; }

if(isset($_GET['add'])) {
    $id = $_GET['add'];
    $_SESSION['cart'][$id] = ($_SESSION['cart'][$id] ?? 0) + 1;
}
?>
<h2>Shopping Cart</h2>
<p>Items in cart: <?php echo array_sum($_SESSION['cart']); ?></p>
<a href="?add=1">Add Book 1</a> | <a href="?add=2">Add Book 2</a>