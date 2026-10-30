<?php
session_start();
if(!isset($_SESSION['cart'])) { $_SESSION['cart'] = []; }
if(isset($_GET['add'])) {
    $id = $_GET['add'];
    $_SESSION['cart'][$id] = ($_SESSION['cart'][$id] ?? 0) + 1;
}
?>
<h2>Cart Count: <?php echo array_sum($_SESSION['cart']); ?></h2>
<a href="?add=1">Add Product 1</a>