<?php
require_once '2.php';
$result = $conn->query("SELECT * FROM products");
?>
<table border="1" cellpadding="10">
    <tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th></tr>
    <?php while($row = $result->fetch_assoc()): ?>
    <tr>
        <td><?php echo $row['id']; ?></td>
        <td><?php echo htmlspecialchars($row['name']); ?></td>
        <td><?php echo htmlspecialchars($row['category']); ?></td>
        <td>$<?php echo $row['price']; ?></td>
    </tr>
    <?php endwhile; ?>
</table>