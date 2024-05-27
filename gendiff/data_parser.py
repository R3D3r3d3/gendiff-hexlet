import os
import json
import yaml

TYPE_JSON = ".json"
TYPE_YML = (".yml", ".yaml")


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def parse_data(file_path):
    with open(file_path) as file_in:
        if get_file_extension(file_path) == TYPE_JSON:
            data = json.load(file_in)

        elif get_file_extension(file_path) in TYPE_YML:
            data = yaml.safe_load(file_in.read())

        else:
            raise ValueError("Unsupported file format")

    return data
