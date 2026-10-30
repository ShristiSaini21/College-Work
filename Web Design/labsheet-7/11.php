<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$limit = 5;
$page = $_GET['page'] ?? 1;
$start = ($page - 1) * $limit;
$res = $conn->query("SELECT * FROM books LIMIT $start, $limit");
?>
<ul>
    <?php while($row = $res->fetch_assoc()): ?>
        <li><?php echo $row['title']; ?></li>
    <?php endwhile; ?>
</ul>
<a href="?page=1">1</a> <a href="?page=2">2</a>