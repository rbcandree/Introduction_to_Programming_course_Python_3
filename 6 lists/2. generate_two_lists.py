"""
In the followin program, two variables are initalized with random integers: n1 and n2. 
You can assume, that the value of n2 is always larger than value of n1.

Your job is to generate two lists:
1. A list that contains all values between [n1, n2] in increasing order. Store a reference to this list into variable list1.
2. A list that contains all values between [n2, n1] in decreasing order. Store a reference to this list into variable list2.
Note, that you need to indent the lines in your solution with two spaces by yourself to match the indentation of the code outside your solution.

thislist = [100, 50, 65, 82, 23]
thislist.sort() # sorts the list in numerical order
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # sorts the list in reverse order
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) # sorts the list in reverse order
print(thislist)
"""
import random
for i in range(3):
    n1 = random.randint(1,10)
    n2 = random.randint(20,30)
    
    print ("n1:",n1)
    print ("n2:",n2)
    
    list1 = list(range(n1, n2 + 1))
    list2 = list(range(n2, n1 - 1, -1))    

    print ("List1:",list1)
    print ("List2:",list2)
    
    print ("")