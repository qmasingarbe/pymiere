import os, json

TYPE_CORRESPONDENCE = {"string": "str", "boolean": "bool", "number": "float", "any": "any", "undefined": "None"}


def write_json_file(filepath, data):
    if not os.path.isdir(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def read_json_file(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


class MyStr(str):
    """Subclass of string to add code line quicker"""
    def add_line(self, content, indent=0):
        return MyStr(self + "\n" + indent*4*" " + content)

    def add_empty_line(self, number=1):
        return MyStr(self + "\n"*number)