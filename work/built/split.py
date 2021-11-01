def reorder(string):
    res = []
    for line in string.split('\n')[1:]:
        res.append(line.split(',', maxsplit=2))
    return res


def s(c):
    return [item.split(',', maxsplit=2) for item in c.split('\n')[1:]]


string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

print(s(string))

# res = []
# for line in string.split('\n')[1:]:
#     res.append(line.split(',', maxsplit=2))

# print(res)

# for name, phone, adress in res:
#     print(adress)
