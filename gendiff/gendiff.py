import json


def bool_to_lower(val):
    """business logics requires bool values represent in lower case"""

    if type(val) is bool:
        return str(val).lower()
    return val


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        f1 = json.load(f1)
        f2 = json.load(f2)
        keys = sorted(f1|f2)
        result = "{\n"
        for k in keys:
            if k in set(f1.keys()) & set(f2.keys()):
                if f1[k] == f2[k]:
                    result += f"  {k}: {bool_to_lower(f1[k])}\n"
                else:
                    result += f"- {k}: {bool_to_lower(f1[k])}\n"
                    result += f"+ {k}: {bool_to_lower(f2[k])}\n"
            elif k in (set(f1.keys()) - set(f2.keys())):
                result += f"- {k}: {bool_to_lower(f1[k])}\n"
            else:
                result += f"+ {k}: {bool_to_lower(f2[k])}\n"
        result += "}"
        return result
