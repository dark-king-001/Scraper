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
    def __init__(self,permalink):
        f = open(permalink)
        self.data = json.load(f)
        self.operation_length = len(self.data['items'])
        self.links = []
        f.close()
    def download(self):
        for i in range(0,len(self.links),1):
            try: 
                name = self.links[i][8::1]
                link = self.links[i]
                print(f'Num{i}:downloading {name}')
                wk.Worker(f'mkdir downloads/{name} && exit')
                time.sleep(0.1)
                wk.Worker(f'python3 download.py /home/piyush/Desktop/Manual_scrape/downloads/{name} {link}')
            except Exception as e:
                # Handle other exceptions here
                print(f"Error: {e}")
                break
    def linkLoad(self):
        for obj in self.data['items']:
            self.links.append(obj['permalink'])
            print(f'{len(self.links)} loaded successfully')

