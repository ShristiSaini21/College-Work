<?php
// Write a PHP script that handles file uploads (`$_FILES`), validates file size and extension, and stores images in an Apache server directory.[cite: 13]
$uploadMessage = "";
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['image'])) {
    $file = $_FILES['image'];
    $fileName = $file['name'];
    $fileTmpName = $file['tmp_name'];
    $fileSize = $file['size'];
    $fileError = $file['error'];

    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    $allowed = ['jpg', 'jpeg', 'png', 'gif'];

    if (in_array($fileExt, $allowed)) {
        if ($fileError === 0) {
            if ($fileSize < 2097152) { // Less than 2MB
                $fileDestination = 'uploads/' . uniqid('', true) . '.' . $fileExt;
                if (!is_dir('uploads')) {
                    mkdir('uploads', 0777, true);
                }
                if (move_uploaded_file($fileTmpName, $fileDestination)) {
                    $uploadMessage = "File uploaded successfully!";
                } else {
                    $uploadMessage = "Failed to move uploaded file.";
                }
            } else {
                $uploadMessage = "File size is too large (Max 2MB).";
            }
        } else {
            $uploadMessage = "There was an error uploading your file.";
        }
    } else {
        $uploadMessage = "Invalid file extension. Allowed: jpg, jpeg, png, gif.";
    }
}
?>
<!DOCTYPE html>
<html>
<head><title>File Upload</title></head>
<body>
    <form method="POST" enctype="multipart/form-data">
        <h2>Upload Image</h2>
        <p><?php echo $uploadMessage; ?></p>
        <input type="file" name="image" required><br><br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>