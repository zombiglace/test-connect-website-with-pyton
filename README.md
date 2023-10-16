# test-connect-website-with-pyton

The import urllib.request statement imports the urllib.request module, which provides functions for working with URLs.

The link variable stores the URL that you want to connect to.

The connect() function is defined to establish a connection to the specified URL. It uses a try-except block to handle any exceptions that may occur during the connection attempt.

Inside the try block, urllib.request.urlopen(link) is called to open a connection to the URL. If the connection is successful, the function returns True.

If an exception occurs during the connection attempt (e.g., if the URL is not accessible), the except block is executed, and the function returns False.

Finally, the script checks the return value of the connect() function. If it is True, it prints "Connected". Otherwise, it prints "Failed to connect".

This code can be useful for checking if a given URL is accessible or not.
