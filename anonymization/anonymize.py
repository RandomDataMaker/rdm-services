import hashlib


def anonymize(obj, anonymize_array):
    anonymize_array = anonymize_array.split(',')
    tmp_hash = ""
    if anonymize_array[0] == 'none':
        return obj

    for item in anonymize_array:
        tmp_hash += str(obj[item])
        obj[item] = ""

    obj["hash"] = hashlib.sha3_256(tmp_hash.encode('utf-8')).hexdigest()
    return obj
