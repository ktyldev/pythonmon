import json


def get_data(json_file):
    with open(json_file) as data_file:
        data = json.load(data_file)
        return data
