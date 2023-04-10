import json

input_files = [
    'permalink/files/volume1.json',
    'permalink/files/volume2.json',
    'permalink/files/volume3.json',
    'permalink/files/volume4.json',
    'permalink/files/volume5.json',
    'permalink/files/volume6.json',
    'permalink/files/volume7.json'
]
output_file = 'permalink/permalink.json'

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
with open(output_file, "w") as f:
    json.dump({"links":links}, f)