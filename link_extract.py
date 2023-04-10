import json

input_files = [
    'permalink/files/studyhelpinghand.txt',
]
output_file = 'permalink/permalink.json'

def fromJson():
    links = []
    try:
        for file in input_files:
            with open(file) as f:
                data = json.load(f)
                for obj in data['items']:
                    links.append(obj['permalink'])
            print(f'{file} done')
    except Exception as e:
        # Handle other exceptions here
        print(f"Error: {e}")
    return links
def fromTXT():
    links = []
    try:
        for file in input_files:
            with open(file) as f:
                data = f.read().split('\n')
                for obj in data:
                    if obj[:8] == 'https://':
                        links.append(obj)
            print(f'{file} done')
    except Exception as e:
        # Handle other exceptions here
        print(f"Error: {e}")
    f.close()
    return links
def save(links):
    with open(output_file, "w") as f:
        json.dump({"links":links}, f)

save(fromTXT())