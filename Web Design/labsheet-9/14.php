<?php
if(isset($_POST['upload'])) {
    $file = $_FILES['image'];
    $fileName = time() . "_" . basename($file['name']);
    $target = "uploads/" . $fileName;
    if($file['size'] < 2000000) {
        move_uploaded_file($file['tmp_name'], $target);
        echo "Image uploaded successfully!";
    }
}
?>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="image" required><br>
    <button type="submit" name="upload">Upload</button>
</form>