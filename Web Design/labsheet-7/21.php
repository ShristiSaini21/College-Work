<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$res = $conn->query("SELECT SUM(total_price) as revenue, COUNT(id) as total_orders FROM orders");
$data = $res->fetch_assoc();
?>
<h2>Sales Summary Report</h2>
<p>Total Revenue: $<?php echo $data['revenue'] ?? 0; ?></p>
<p>Total Orders: <?php echo $data['total_orders'] ?? 0; ?></p>