<form id="regForm" onsubmit="return validateForm()">
    <input type="text" id="username" placeholder="Username">
    <input type="password" id="password" placeholder="Password">
    <button type="submit">Register</button>
</form>
<script>
function validateForm() {
    let u = document.getElementById('username').value;
    let p = document.getElementById('password').value;
    if(u === "" || p === "") {
        alert("All fields must be filled out");
        return false;
    }
}
</script>