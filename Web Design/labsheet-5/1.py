# Configure Apache web server to execute Python CGI scripts or WSGI applications (mod_wsgi) and verify with a 'Hello World' Python script.
print("Content-Type: text/html\n")
print("<h1>Hello World from Python CGI Script!</h1>")
print("<p>Apache web server is configured to execute Python scripts.</p>")