<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
$search = $_GET['search'] ?? '';
$res = $conn->query("SELECT * FROM books WHERE title LIKE '%$search%' OR author LIKE '%$search%'");
?>
<form method="GET">
    <input type="text" name="search" placeholder="Search by title or author...">
    <button type="submit">Search</button>
</form>
<ul>
    <?php while($row = $res->fetch_assoc()): ?>
        <li><?php echo $row['title']; ?> by <?php echo $row['author']; ?></li>
    <?php endwhile; ?>
</ul>