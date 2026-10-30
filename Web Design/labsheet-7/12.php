<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$res = $conn->query("SELECT * FROM orders WHERE user_id = 1");
?>
<h2>Order History</h2>
<ul>
    <?php while($row = $res->fetch_assoc()): ?>
        <li>Order ID: <?php echo $row['id']; ?> - Status: <?php echo $row['status']; ?></li>
    <?php endwhile; ?>
</ul>