"""
Example about list references, passing them as parameters and changing references.
"""

def main():
    a = [1,3,5,7]   # Array a is created. The len of array is 4.
    b = [5,8,2,1]   # Array b is created. The len of array is 4
    increase_all(a) # Method call increase_all - automatically moving to function increase_all(t), --> line def increase_all(t):
                    # returns value, after executing and stopping function def increase_all(t):
    b = a           # List b is set to point to list a. A reference to a list is copied from a to b.
    a[1] = 1        # The value of element with index 1 in list a is changed to 1 --> a = [2,1,6,8]
    b[0] = b[1] * 2 # The value of element with index 1 in list b is changed to 2 (1 * 2). b = a = [2,1,6,8]
    print ("a[0]:"+a[0]+" and b[0]:"+b[0]) #Output: a[0]:2 and b[0]:2
    print ("a[1]:"+a[1]+" and b[1]:"+b[1]) #Output: a[1]:1 and b[1]:1
    print ("a[2]:"+a[2]+" and b[2]:"+b[2]) #Output: a[2]:6 and b[2]:6
    print ("a[3]:"+a[3]+" and b[3]:"+b[3]) #Output: a[3]:8 and b[3]:8
    print (a)       # Output: [2,1,6,8]

def increase_all(t):
    for i in range(0,len(t),1):     # Initialising variable i with value 0.For loop rotates. Condition ( i<t.length) --> (0 < 4 ) is True. Execution continues inside the block.
                                    # The value of variable i is changed to 1. For loop rotates. Condition ( i<t.length) --> (1 < 4 ) is True. Execution continues inside the block.
                                    # The value of variable i is changed to 2. For loop rotates. Condition ( i<t.length) --> (2 < 4 ) is True. Execution continues inside the block.
                                    # The value of variable i is changed to 3. For loop rotates. Condition ( i<t.length) --> (3 < 4 ) is True. Execution continues inside the block.
                                    # The value of variable i is changed to 4. For loop rotates. Condition ( i<t.length) --> (4 < 4 ) is False. The block is not executed.
        t[i] = t[i] + 1             # The value of cell 0 in array t (a) is changed to 2 (1 + 1). t = a = [2,3,5,7]
                                    # The value of cell 1 in array t is changed to 4 (3 + 1). t = a = [2,4,5,7]
                                    # The value of cell 2 in array t is changed to 6 (5 + 1). t = a = [2,4,6,7]
                                    # The value of cell 3 in array t is changed to 8 (7 + 1). t = a = [2,4,6,8]
# next line after the terminating (stopping) of function.
# function ends.

"""
Questions:
1. What is the last index of a?
    a = [1,3,5,7]
Answer: 3

2. What is the address where b is referring to?
    increase_all(a)
Answer: 002 (it is an id of b in the Ville's interface, in Python it would be an print(id(b)))

3. What is happening in this line?
    b = a
Answer: A reference to a list is copied from a to b.

4. Which of the following values is displayed in this line?
     print ("a[0]:"+a[0]+" and b[0]:"+b[0])
Answer: a[0]:2 and b[0]:2
"""