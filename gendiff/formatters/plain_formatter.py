from gendiff.formatters.helpers import plain_helper
from gendiff.formatters.helpers import repr_helper


def plain_diff(data, name=""):
    data.sort(key=lambda x: x["name"])
    result = list()
    for dct in data:
        if dct["status"] == "nested":
            new_name = f"{name}{dct['name']}."
            data_nested = plain_diff(dct['children'], new_name)
            result.append(data_nested)

        if dct["status"] == "added":
            name2 = name + dct['name']
            value = plain_helper(dct["data"])
            res = f"Property {repr_helper(name2)} was added with value: \
{repr_helper(value)}"
            result.append(res)
        if dct["status"] == "deleted":
            name2 = name + dct['name']
            result.append(f"Property {repr_helper(name2)} was removed")
        if dct["status"] == "changed":
            name2 = name + dct['name']
            v_before = plain_helper(dct["data_before"])
            v_after = plain_helper(dct["data_after"])
            res = f"Property {repr_helper(name2)} was updated. \
From {repr_helper(v_before)} to {repr_helper(v_after)}"
            result.append(res)

    result = [x for x in result if x]

    return "\n".join(result)
