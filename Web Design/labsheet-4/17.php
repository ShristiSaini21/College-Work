<?php
// Write a PHP script that exports MySQL database table data into a downloadable CSV file format.[cite: 13]
$host = 'localhost';
$db   = 'college_db';
$user = 'root';
$pass = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $stmt = $pdo->query("SELECT * FROM students");
    $students = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (isset($_GET['export']) && $_GET['export'] == 'true') {
        header('Content-Type: text/csv');
        header('Content-Disposition: attachment; filename="students_report.csv"');
        
        $output = fopen('php://output', 'w');
        if (!empty($students)) {
            fputcsv($output, array_keys($students[0])); // Column headers
            foreach ($students as $row) {
                fputcsv($output, $row);
            }
        }
        fclose($output);
        exit();
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
<!DOCTYPE html>
<html>
<head><title>Export CSV</title></head>
<body>
    <h2>Export Students Table to CSV</h2>
    <a href="?export=true"><button>Download CSV Report</button></a>
</body>
</html>