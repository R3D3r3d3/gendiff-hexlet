def get_diff(dict1, dict2):
    """Get difference between two dictionaries in one list."""
    result = []
    # union keys
    keys = dict1.keys() | dict2.keys()
    for key in keys:
        dct = {'name': key}
        if key not in dict1:
            dct['status'] = 'added'
            dct['data'] = dict2[key]
        elif key not in dict2:
            dct['status'] = 'deleted'
            dct['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            dct['status'] = 'nested'
            dct['children'] = get_diff(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            dct['status'] = 'not changed'
            dct['data'] = dict1[key]
        else:
            dct['status'] = 'changed'
            dct['data_before'] = dict1[key]
            dct['data_after'] = dict2[key]
        result.append(dct)
    return result
