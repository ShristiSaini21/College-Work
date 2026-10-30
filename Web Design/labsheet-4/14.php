<?php
/* Configure MySQL user privileges by creating a dedicated database user with restricted permissions (`SELECT, INSERT, UPDATE`) for the web application.[cite: 13] */
/*
  Run these queries directly in MySQL/phpMyAdmin:
  
  CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_password';
  GRANT SELECT, INSERT, UPDATE ON college_db.* TO 'app_user'@'localhost';
  FLUSH PRIVILEGES;
*/
echo "MySQL user privilege configuration commands defined in code comments.";
?>