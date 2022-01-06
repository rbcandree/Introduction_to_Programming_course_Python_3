"""
Write a procedure join(d1,d2), which receives two dictionaries as an argument. 
The procedure inserts all items from dictionary d2 into dictionary d1, providing that the key does not already exist in d1. 
If the key already exists in d1, the item is ignored.
For example, if called with dictionaries:

d1 = {1: 10, 2: 20, 3: 30}
d2 = {1: -10, 4: -40}
...after the procedure is executed, d1 will contain items:
d1 == {1: 10, 2: 20, 3: 30, 4: -40}
"""
import random
def join(d1, d2):
    d1 = d1.update(d2)
    return d1

def output(d, ignore = True):
    if ignore:
        print ("{", end = "")
    for key in sorted(d.keys()):
        print (str(key) + ":" + str(d[key]) + ", ", end = "")
    print ("}")
    
def test():
    d1 = {}
    d2 = {}
    for i in range(random.randint(6,12)):
        d1[random.randint(1,15)] = random.randint(-100,0)
    for i in range(random.randint(8,14)):
        d2[random.randint(5,20)] = random.randint(1,100)
    print ("Dictionaries before:")
    output(d1)
    output(d2)
    join(d1,d2)
    print ("")
    print ("Dictionary after:")
    output(d1)

test()