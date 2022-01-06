"""
Construct a function create_tuple, that receives three integer type arguments value1, value2 and value3. 
The function creates a tuple where the first item is value1 and the second item the sum of values 2 and 3. 
Finally this tuple is returned.
"""
def create_tuple(value1, value2, value3):
    first = value1
    second = value2 + value3
    tuple = (first, second)
    return tuple