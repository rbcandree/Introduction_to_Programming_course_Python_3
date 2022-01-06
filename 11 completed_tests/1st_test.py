# Numbers
# What is the *type* of the result of the expression 3 + 1.5 + 4? 
# Answer: float

# What would you use to find a number’s square root, as well as its square?
# Square root:  
int(9 ** 0.5)                       # Output: 3
# Square:       
5 ** 2                              # Output: 25

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
s[1]
# Reverse the string 'hello' using slicing:
s ='hello'
s[::-1]                             # Output: 'olleh'

# Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
# Print out the 'o'
# Method 1:
s[-1]
# Method 2:
s[len(s)-1]                         # Output: 'o'

# Question: Are strings mutable?
# Strings are not mutable.

# Lists
# Build this list [0,0,0] two separate ways.
# Method 1:
list1 = [0,0]
list1.append(0)
list1                               # Output: [0, 0, 0]
# Method 2:
list2 = [0]
list2 = list2*3
list2                               # Output: [0, 0, 0]

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
list3                               # Output: [1, 2, [3, 4, 'goodbye']]

# Sort the list below:
# Method 1:
list4 = [5,3,4,6,1]
list4.sort()
list4                               # Output: [1, 3, 4, 5, 6]
# Method 2:
list4 = [5,3,4,6,1]
sorted(list4)                       # Output: [1, 3, 4, 5, 6]

# Question:                                                                     0  1    2
# How do you index a nested list? For example if you want to grab 2 from my_list = [1, 1, [1, 2]]?
#                                                                                      0  1
# Answer: I would just add another set of brackets for indexing the nested list, for example: my_list[2][1] . 

# Build a list comprehension by deconstructing a for loop within a []:
matrix = [[0, 5, 10], [2, 4, 6], [3, 9, 15]]
column1 = [row[0] for row in matrix]
column1_same = [x[0] for x in matrix]
print(column1)                # Output: [0, 2, 3]
print(column1_same)           # Output: [0, 2, 3]

# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'key':'hello'}
# Grab 'hello'
d['key']                            # Output: 'hello'

# Grab 'hello'
d = {'k1':{'k2':'hello'}}
d['k1']['k2']                       # Output: 'hello'

# Grab 'hello'
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1][0]        # Output: 'hello'

# Grab 'hello'
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]  # Output: 'hello'

# Can you sort a dictionary? Why or why not?
# Answer: No, because normal dictionaries are mappings, not a sequence.  

# Tuples
# What is the major difference between tuples and lists?
# Answer: Tuples are immutable.

# How do you create a tuple?
# By using a (,) or the function tuple().

# Sets
# What is unique about a set?
# Answer: Sets are unordered collections of unique elements. They don't allow for duplicate items.

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)                          # Output: {1, 2, 3, 4, 11, 22, 33}

# Booleans
# What will be the resulting Boolean of the following pieces of code?
2 > 3       # ---> False
3 <= 2      # ---> False
3 == 2.0    # ---> False
3.0 == 3    # ---> True
4**0.5 != 2 # ---> False

# What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
l_one[2][0] >= l_two[2]['k1']       # Output: False (because 3 >=4)