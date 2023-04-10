# importing the libraries
from bs4 import BeautifulSoup
import json
import requests

f = open('permalink/permalink.json')
data = json.load(f)
print(data['links'][0][8::1])

# Open the txt file in append mode
with open("dataset/studyhelpinghand.txt", "a") as f:
    # Read the HTML file and parse it with BeautifulSoup
    for link in data['links']:
        path = link[8::1]
        try:
            with open(f"downloads/{path}/index.html") as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                
                # Extract the links from the HTML and store them in a list
                lines = []
                for line in soup.find_all('p'):
                    lines.append(line.get_text())
                for line in soup.find_all('li'):
                    lines.append(line.get_text())
                
                # Loop through the list of links and write each link to the txt file
                for line in lines:
                    f.write(line + "\n")
                print(f"completed downloads/{path}/index.html")
        except Exception as e:
            # Handle other exceptions here
            print(f"Error: {e}")

# Close the file after you are done writing
f.close()