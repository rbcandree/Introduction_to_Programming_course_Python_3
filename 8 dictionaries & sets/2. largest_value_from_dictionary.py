"""
Write a function get_largest_value(d), which returns the largest value stored in the dictionary received as an argument.
"""
import random
def get_largest_value(d):
    largestValue = max(d.values())
    get_largest_value = largestValue
    return get_largest_value
  
def test():
    d = {}
    for i in range(random.randint(10,15)):
        key = random.randint(1,1000)
        value = random.randint(-100,100)
        d[key] = value
    print ("Dictionary:", d)
    print ("Largest value:", get_largest_value(d))
    
for i in range(3):
    test()