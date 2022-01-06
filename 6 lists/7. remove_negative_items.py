"""
Write a procedure:

def remove_negatives(list_of_integers):

...which gets a list of integers as an argument, and removes all items with value smaller than zero from that list.
"""
import random
def remove_negatives(list_of_integers):
  list_of_integers[:] = [x for x in list_of_integers if x > 0]

l = []
for i in range(0, random.randint(15,25)):
  l.append(random.randint(-15,15))

print ("Before:", l)
remove_negatives(l)
print ("After:", l)

"""
list_of_integers[:] = [x for x in list_of_integers if x > 0]

By assigning to list_of_integers[:], list_of_integers still reference to the same list object, with contents modified. 
By assigning to list_of_integers, list_of_integers now references to a new list object.

Check out id's:
>>> a_list = []
>>> id(a_list)
32092040
>>> a_list[:] = ['foo', 'bar']
>>> id(a_list)
32092040
>>> a_list = ['foo', 'bar']
>>> id(a_list)
35465096
As you can see, its id doens't change with the slice assignment version.
"""