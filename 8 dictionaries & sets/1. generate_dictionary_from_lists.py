"""
Construct a function that generates a dictionary from two lists received as arguments. 
The items in the first list are used as keys and the items in the second list as values.
"""
keys = (1, 2, 3)
values = (10, 100, 1000)

def dict_from_lists(keys, values):
    d = {}
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        d[key] = value
    return d

print(dict_from_lists(keys, values))