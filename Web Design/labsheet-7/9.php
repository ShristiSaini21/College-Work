<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
if(isset($_POST['update_status'])) {
    $id = $_POST['order_id'];
    $status = $_POST['status'];
    $conn->query("UPDATE orders SET status='$status' WHERE id=$id");
}
$orders = $conn->query("SELECT * FROM orders");
?>
<h2>Manage Orders</h2>
<table border="1">
    <tr><th>ID</th><th>Status</th><th>Action</th></tr>
    <?php while($o = $orders->fetch_assoc()): ?>
    <tr>
        <td><?php echo $o['id']; ?></td>
        <td><?php echo $o['status']; ?></td>
        <td>
            <form method="POST">
                <input type="hidden" name="order_id" value="<?php echo $o['id']; ?>">
                <select name="status"><option>Pending</option><option>Shipped</option><option>Delivered</option></select>
                <button type="submit" name="update_status">Update</button>
            </form>
        </td>
    </tr>
    <?php endwhile; ?>
</table>