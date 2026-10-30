<?php
$conn = new mysqli("localhost", "root", "", "bookstore_db");
if(isset($_POST['submit_review'])) {
    $rating = $_POST['rating'];
    $comment = $_POST['comment'];
    $conn->query("INSERT INTO reviews (rating, comment) VALUES ('$rating', '$comment')");
}
?>
<form method="POST">
    <select name="rating"><option>5 Stars</option><option>4 Stars</option></select><br>
    <textarea name="comment" placeholder="Leave a comment"></textarea><br>
    <button type="submit" name="submit_review">Submit Review</button>
</form>