import json
import time
import Worker as wk
import download as dl

# "items":[
#     {"no":"1",
#     "permalink":"a permanent link from sitemap",
#     "title":"title of the link",
#     "time":"2021-08-16 07:07:22"
#     }
# ]
class scraper:
    def __init__(self):
        f = open('permalink/permalink.json')
        self.data = json.load(f)
        self.operation_length = len(data)
        print(f'starting operation {operation_length}')
        f.close()
    def download(self);
        for i in range(0,self.operation_length,1):
            if self.data['items'][i]['no'].split(' ')[0] != '~':
                number = self.data['items'][i]['no'].split(' ')[1]
            else:
                print("Index out of range")
                continue
            title = self.data['items'][i]['title']
            link = self.data['items'][i]['permalink']
            print(f'downloading {number} - {title}')
            wk.Worker(f'mkdir downloads/{number}')
            time.sleep(0.2)
            dl.load(f'/home/piyush/Desktop/Manual_scrape/downloads/{number}',link)
    
