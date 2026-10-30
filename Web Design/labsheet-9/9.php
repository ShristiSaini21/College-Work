<?php
require_once '2.php';
$id = $_GET['id'] ?? 1;
if(isset($_POST['update'])) {
    $stmt = $conn->prepare("UPDATE products SET name=?, price=? WHERE id=?");
    $stmt->bind_param("sdi", $_POST['name'], $_POST['price'], $id);
    $stmt->execute();
    echo "Updated successfully!";
}
$product = $conn->query("SELECT * FROM products WHERE id=$id")->fetch_assoc();
?>
<form method="POST">
    <input type="text" name="name" value="<?php echo $product['name'] ?? ''; ?>"><br>
    <input type="number" step="0.01" name="price" value="<?php echo $product['price'] ?? ''; ?>"><br>
    <button type="submit" name="update">Update Product</button>
</form>