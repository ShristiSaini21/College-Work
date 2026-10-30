<?php
require_once '2.php';
$limit = 5;
$page = $_GET['page'] ?? 1;
$start = ($page - 1) * $limit;
$res = $conn->query("SELECT * FROM products LIMIT $start, $limit");
?>
<ul>
    <?php while($row = $res->fetch_assoc()): ?>
        <li><?php echo $row['name']; ?></li>
    <?php endwhile; ?>
</ul>
<a href="?page=1">1</a> | <a href="?page=2">2</a>