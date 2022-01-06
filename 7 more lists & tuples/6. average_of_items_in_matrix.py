"""
Write a function average(m), which receives a matrix containing integer items as argument. 
The function calculates and returns the average of the items in the matrix.
"""
import random
def average(m):
    numbers = []
    for row in m:
        for item in row:
            numbers.append(item)
    total = sum(numbers)
    amount = len(numbers)
    avg = total / amount
    return avg

def test():
    l = []
    for i in range(random.randint(3,5)):
        ll = []
        for j in range(random.randint(3,4)):
            ll.append(random.randint(1,10))
        l.append(ll)
    print ("Matrix:",l)
    print ("Average of items:", average(l))

test()
print ("")
test()