import os, json

def write_json_file(filepath, data):
    if not os.path.isdir(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def read_json_file(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data