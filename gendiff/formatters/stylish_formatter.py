from gendiff.formatters.helpers import stylish_helper


def stylish_diff(data, indent_level=0):
    data.sort(key=lambda x: x["name"])
    result = "{\n"
    indent = "  "
    for _ in range(indent_level):
        indent += "    "

    signs = {"not changed": " ", "added": "+", "deleted": "-"}

    for dct in data:
        if dct["status"] == "nested":
            data_nested = stylish_diff(dct["children"], indent_level + 1)
            result += f'{indent}  {dct["name"]}: {data_nested}\n'
        if dct["status"] in signs.keys():
            sign = signs.get(dct["status"])
            value = stylish_helper(dct["data"], indent)
            result += f'{indent}{sign} {dct["name"]}: {value}\n'
        if dct["status"] == "changed":
            value_before = stylish_helper(dct["data_before"], indent)
            value_after = stylish_helper(dct["data_after"], indent)
            ind_1 = ("", " ")[bool(value_before)]
            ind_2 = ("", " ")[bool(value_after)]
            result += f'{indent}- {dct["name"]}:{ind_1}{value_before}\n'
            result += f'{indent}+ {dct["name"]}:{ind_2}{value_after}\n'

    result += indent[:-2] + '}'
    return result
