import json
import time
import Worker as wk

class scraper:
    def __init__(self):
        f = open('permalink/permalink.json')
        self.data = json.load(f)
        self.operation_length = len(self.data['links'])
        print(f'operation length : {self.operation_length}')
        f.close()
    def download(self):
        for i in range(0,self.operation_length,1):
            try: 
                name = self.data['links'][i][8::1]
                link = self.data['links'][i]
                print(f'Num{i}:downloading {name}')
                wk.Worker(f'mkdir downloads/{name} && exit')
                time.sleep(0.1)
                wk.Worker(f'python3 download.py /home/piyush/Desktop/Manual_scrape/downloads/{name} {link}')
            except Exception as e:
                # Handle other exceptions here
                print(f"Error: {e}")
                break
main = scraper()
main.download()