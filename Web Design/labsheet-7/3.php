<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$result = $conn->query("SELECT * FROM books");
?>
<!DOCTYPE html>
<html>
<head><title>Books Grid</title></head>
<body>
    <h2>Available Books</h2>
    <div style="display: flex; gap: 20px;">
        <?php while($row = $result->fetch_assoc()): ?>
            <div style="border: 1px solid #ccc; padding: 10px; width: 150px;">
                <h3><?php echo $row['title']; ?></h3>
                <p>Author: <?php echo $row['author']; ?></p>
                <p>Price: $<?php echo $row['price']; ?></p>
                <a href="4.php?id=<?php echo $row['id']; ?>">View Details</a>
            </div>
        <?php endwhile; ?>
    </div>
</body>
</html>