from gendiff.formatters.stylish_formatter import stylish_diff
from gendiff.formatters.plain_formatter import plain_diff
from gendiff.formatters.json_formatter import json_diff
from gendiff.data_parser import parse_data
from gendiff.diff import get_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    try:
        f1 = parse_data(file_path1)
        f2 = parse_data(file_path2)
    except FileNotFoundError:
        return "One or both files not found"
    except ValueError as e:
        return str(e)
    data_diff = get_diff(f1, f2)
    if format_name == "plain":
        return plain_diff(data_diff)
    if format_name == "json":
        return json_diff(data_diff)
    return stylish_diff(data_diff)
