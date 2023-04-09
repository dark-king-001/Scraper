import json
import time
import Worker as wk
import download as dl

class scraper:
    def __init__(self):
        print("hello")

lol = scraper()
f = open('permalink/permalink.json')
data = json.load(f)

operation_length = len(data['items'])
print(f'starting operation {operation_length}')

for i in range(0,operation_length,1):
    if data['items'][i]['no'].split(' ')[0] != '~':
        number = data['items'][i]['no'].split(' ')[1]
    else:
        print("Index out of range")
        continue
    title = data['items'][i]['title']
    link = data['items'][i]['permalink']
    print(f'downloading Chapter {number} - {title}')
    wk.Worker(f'mkdir downloads/{number}')
    time.sleep(0.2)
    dl.load(f'/home/piyush/Desktop/Manual_scrape/downloads/{number}',link)
    
f.close()