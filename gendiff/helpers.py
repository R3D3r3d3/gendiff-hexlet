def bool_to_str_lower(val, indent=''):
    if val is None:
        return 'null'
    if type(val) is bool:
        return str(val).lower()
    if type(val) is dict:
        indent += '    '
        result = '{\n'
        for key in val.keys():
            value = bool_to_str_lower(val[key], indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
        return result
    return str(val)
