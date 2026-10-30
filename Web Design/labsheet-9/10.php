<?php
require_once '2.php';
if(isset($_GET['delete'])) {
    $id = $_GET['delete'];
    $conn->query("DELETE FROM products WHERE id=$id");
    header("Location: 10.php");
}
$res = $conn->query("SELECT * FROM products");
?>
<table border="1">
<?php while($row = $res->fetch_assoc()): ?>
    <tr>
        <td><?php echo $row['name']; ?></td>
        <td><a href="?delete=<?php echo $row['id']; ?>" onclick="return confirm('Are you sure?')">Delete</a></td>
    </tr>
<?php endwhile; ?>
</table>