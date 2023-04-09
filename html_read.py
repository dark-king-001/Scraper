# importing the libraries
from bs4 import BeautifulSoup
import requests

with open("downloads/1/index.html") as f:
    soup = BeautifulSoup(f, 'html.parser')
    para = []
    for text in soup.find_all('p'):
        para.append(text.get_text())

# Open the txt file in append mode
with open("dataset/story.txt", "a") as f:
    # Read the HTML file and parse it with BeautifulSoup
    for i in range(0,868,1):
        try:
            with open(f"downloads/{i+1}/index.html") as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                
                # Extract the links from the HTML and store them in a list
                lines = []
                for line in soup.find_all('p'):
                    lines.append(line.get_text())
                
                # Loop through the list of links and write each link to the txt file
                for line in lines:
                    f.write(line + "\n")
                print(f"completed downloads/{i+1}/index.html")
        except Exception as e:
            # Handle other exceptions here
            print(f"Error: {e}")

# Close the file after you are done writing
f.close()