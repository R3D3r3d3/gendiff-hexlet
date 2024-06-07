def stylish_helper(val, indent=''):
    if val is None:
        return 'null'
    if type(val) is bool:
        return str(val).lower()
    if type(val) is dict:
        indent += '    '
        result = '{\n'
        for key in val.keys():
            value = stylish_helper(val[key], indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
        return result
    return str(val)


def plain_helper(val):
    if val is None:
        return 'null'
    if type(val) is bool:
        return str(val).lower()
    if type(val) is dict:
        return '[complex value]'
    return str(val)


def repr_helper(val):
    if val in ("null", "true", "false", "[complex value]"):
        return val
    return f"'{val}'"
