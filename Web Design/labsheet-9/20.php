<!DOCTYPE html>
<html>
<body>
    <input type="text" id="search" placeholder="Live search..." onkeyup="liveSearch(this.value)">
    <div id="results"></div>
    <script>
        function liveSearch(str) {
            if(str.length == 0) { document.getElementById("results").innerHTML = ""; return; }
            fetch("search_backend.php?q=" + str)
            .then(response => response.text())
            .then(data => { document.getElementById("results").innerHTML = data; });
        }
    </script>
</body>
</html>