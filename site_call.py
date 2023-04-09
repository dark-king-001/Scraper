import urllib.error
import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as connection:
        code = connection.getcode()
        print(sys.argv[1],code)
        # Do something with the connection
except urllib.error.HTTPError as e:
    # Handle the HTTP error here
    print(f"HTTP error: {e.code} {e.reason}")
except urllib.error.URLError as e:
    # Handle other URL errors here
    print(f"URL error: {e.reason}")
except Exception as e:
    # Handle other exceptions here
    print(f"Error: {e}")