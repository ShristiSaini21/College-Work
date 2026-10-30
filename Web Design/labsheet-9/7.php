<?php
require_once '2.php';
if(isset($_POST['add_product'])) {
    $stmt = $conn->prepare("INSERT INTO products (name, category, price) VALUES (?, ?, ?)");
    $stmt->bind_param("ssd", $_POST['name'], $_POST['category'], $_POST['price']);
    $stmt->execute();
    echo "Product added successfully!";
}
?>
<form method="POST">
    <input type="text" name="name" placeholder="Product Name" required><br>
    <input type="text" name="category" placeholder="Category" required><br>
    <input type="number" step="0.01" name="price" placeholder="Price" required><br>
    <button type="submit" name="add_product">Add Product</button>
</form>