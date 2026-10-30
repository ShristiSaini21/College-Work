<?php
require_once '2.php';
$sort = $_GET['sort'] ?? 'name';
$order = $_GET['order'] ?? 'ASC';
$res = $conn->query("SELECT * FROM products ORDER BY $sort $order");
?>
<table border="1">
    <tr><th><a href="?sort=name&order=<?php echo $order=='ASC'?'DESC':'ASC'; ?>">Name</a></th></tr>
    <?php while($row = $res->fetch_assoc()): ?>
    <tr><td><?php echo $row['name']; ?></td></tr>
    <?php endwhile; ?>
</table>