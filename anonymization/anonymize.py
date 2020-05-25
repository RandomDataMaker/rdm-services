import hashlib


def anonymize(obj, anonymize_array):
    anonymize_array = anonymize_array.split(',')
    tmp_hash = ""
    if anonymize_array[0] == 'none':
        return obj

    result = dict()
    for obj_key in obj.keys():
        if obj_key in anonymize_array:
            tmp_hash += str(obj[obj_key])
        else:
            result[obj_key] = obj[obj_key]

    result["sha3_256"] = hashlib.sha3_256(tmp_hash.encode('utf-8')).hexdigest()
    return result
