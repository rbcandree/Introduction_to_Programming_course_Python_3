"""
Write a function def get_strings(mixed_list):, which returns a new list with all the string type items in the mixedList given as an argument. 
The order of the string items must match the original list. For example, if called with a list like this...
 
[1, 'a', 2, 'b', True, 'e']
...the function should return a list like this:

['a', 'b', 'e']

Version2 with import string:
def get_strings(mixed_list):
  mixed_list[:] = [x for x in mixed_list if (type(x) == str)]
  return mixed_list
"""
import random
import string

def get_strings(mixed_list):
  mixed_list[:] = [x for x in mixed_list if (type(x) == str)]
  return mixed_list

l = []
s = string.ascii_letters
for i in range(random.randint(15,25)):
   r = random.randint(0,2)
   if r == 0:
     ind = random.randint(0, len(s) -1 )
     l.append(s[ind : ind + random.randint(1, 4) ])
   elif r == 1:
      l.append(random.randint(-50,50))
   else:
      l.append(random.choice([True, False, 1.0 / random.randint(1, 10) ]))

print ("Whole list:", l)
print ("Strings only:" , get_strings(l))