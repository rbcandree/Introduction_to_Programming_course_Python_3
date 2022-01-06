"""
Write a function with signature
def sum_of_even(m):
 
which calculates and returns the sum of all even numbers in the list given as an argument. 
For example, if the function was called with argument
[1, 2, 3, 4, 5, 6]
...it would return 12 (since 2 + 4 + 6 = 12).
"""
import random
def sum_of_even(m):
    new_list = [x for x in m if (x % 2 == 0)]
    sum_even = sum(new_list)
    return sum_even
    
l = []
for i in range(0, random.randrange(18,25)):
  l.append(random.randrange(1,16))
  
print ("List:",l)
print ("Sum of even values:",sum_of_even(l))