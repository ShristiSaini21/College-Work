<?php
// Configure PHP extensions (such as `mysqli`, `pdo_mysql`, `mbstring`, `curl`) in `php.ini` and verify their active status.[cite: 13]
echo "<h2>PHP Extensions Status</h2>";
$extensions = ['mysqli', 'pdo_mysql', 'mbstring', 'curl'];

foreach ($extensions as $ext) {
    if (extension_loaded($ext)) {
        echo "<p style='color:green;'>Extension <b>$ext</b> is ENABLED.</p>";
    } else {
        echo "<p style='color:red;'>Extension <b>$ext</b> is DISABLED.</p>";
    }
}
?>