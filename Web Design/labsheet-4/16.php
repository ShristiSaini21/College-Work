<?php
// Implement cookie management in PHP (`setcookie()`) to store and retrieve user preferences like theme color.[cite: 13]
if (isset($_POST['theme'])) {
    $theme = $_POST['theme'];
    setcookie('theme_preference', $theme, time() + (86400 * 30), "/"); // 30 days
    header("Refresh:0"); // Refresh to apply cookie
}

$currentTheme = isset($_COOKIE['theme_preference']) ? $_COOKIE['theme_preference'] : 'light';
$bgColor = ($currentTheme == 'dark') ? '#333' : '#fff';
$textColor = ($currentTheme == 'dark') ? '#fff' : '#000';
?>
<!DOCTYPE html>
<html style="background-color: <?php echo $bgColor; ?>; color: <?php echo $textColor; ?>;">
<head><title>Cookie Preference</title></head>
<body>
    <h2>Theme Preference using Cookies</h2>
    <form method="POST">
        <button type="submit" name="theme" value="light">Light Theme</button>
        <button type="submit" name="theme" value="dark">Dark Theme</button>
    </form>
    <p>Current Theme: <?php echo ucfirst($currentTheme); ?></p>
</body>
</html>