<?php
require_once '2.php';
$search = $_GET['search'] ?? '';
$min = $_GET['min'] ?? 0;
$max = $_GET['max'] ?? 10000;
$stmt = $conn->prepare("SELECT * FROM products WHERE name LIKE ? AND price BETWEEN ? AND ?");
$searchTerm = "%$search%";
$stmt->bind_param("sdd", $searchTerm, $min, $max);
$stmt->execute();
$res = $stmt->get_result();
?>
<form method="GET">
    <input type="text" name="search" placeholder="Search name...">
    <input type="number" name="min" placeholder="Min Price">
    <input type="number" name="max" placeholder="Max Price">
    <button type="submit">Filter</button>
</form>