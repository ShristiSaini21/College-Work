<?php
// Test Apache server performance and error logging by examining `error.log` and `access.log` files during simulated requests.[cite: 13]
/*
  XAMPP Apache log file paths:
  Error Log: C:/xampp/apache/logs/error.log
  Access Log: C:/xampp/apache/logs/access.log
*/
echo "<h2>Apache Log Files Information</h2>";
echo "<p>Error and access log directories are located inside your XAMPP Apache installation folder.</p>";

// Triggering a sample PHP warning to test error logging
trigger_error("Simulated test error for Apache error log verification.", E_USER_WARNING);
?>