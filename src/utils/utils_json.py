import os

import json


def read_json(filename: str):
    """
    Read json file
    :param filename: json file name
    :return: json data
    """
    json_file = os.path.join(filename)
    with open(json_file) as f:
        data = json.load(f)

    return data


def print_json(data: any, tag=''):
    """
    Pretty print json data
    :param data: json data
    :param tag: log tag
    :return: None
    """
    print(tag, json.dumps(data, indent=2, sort_keys=True))


# Pretty print json data to file
def write_json(filename: str, data: any):
    """
    Write json data to file
    :param filename: json file name
    :param data: json data
    :return: None
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
