"""
Write a function with signature def minimum_maximum(integer_list):, 
which returns the minimum and the maximum value of items in the integer_list given as an argument. 
The values should be returned in a tuple, where minimum value is the first item and the maximum value the second.
"""
import random
def minimum_maximum(integer_list):
    lowestValue = min(integer_list)
    highestValue = max(integer_list)
    minimum_maximum = (lowestValue, highestValue)
    return minimum_maximum

l = []
for i in range(random.randint(15,25)):
  l.append(random.randint(-150,150))
           
print ("List:", l)
print ("Minimum and maximum:",minimum_maximum(l))