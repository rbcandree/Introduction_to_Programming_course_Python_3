# 1. Which of the following expressions will evaluate into False?
# Answer:
a = isinstance(3, float)
print(a) 

# 2. What is the length of the list lst after following statement is executed?
lst = [[1,2,3], [4,5,6], [7,7]]
# Answer: 3

# 3. Which of the following is the correct way to reference the first item in the second row of matrix m?
# Answer: m[1][0]

# 4. What value will be stored in variable x after the following program code is executed?
x = 0
m = [[1,2],[3,4]]
for r in m:
  for v in r:
    x = x + v
# Answer: 10
# 1. 0 + 1 = 1
# 2. 1 + 2 = 3
# 3. 3 + 3 = 6
# 4. 6 + 4 = 10

# 5. Which of the following objects are mutable?
# Answer: 
["hello", "hi"]
[1, 2]
[True, False]
# Info: 
# Objects of built-in type that are mutable are:
# Lists
# Sets
# Dictionaries
# User-Defined Classes (It purely depends upon the user to define the characteristics) 

# Objects of built-in type that are immutable are:
# Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
# Strings
# Tuples
# Frozen Sets
# User-Defined Classes (It purely depends upon the user to define the characteristics)

# 6. Assume a tuple 'tup' is initialized with the following statement:
tup = (1,3,2)
# Which of the following operations are permitted with the tuple?
s = len(tup)
x = tup[3]            # NO, wrong indexing
sum = tup[0] + tup[2]
tup[1] = 24           # NO, tuple is immutable
print (tup[0])
tup.sort()            # NO, Python has only two built-in methods for tuples: count() and index()

# 7. What will the following program output?
mm = [[1,2],[3,4],[5,6]]
mm.reverse()
print (mm[0][0])
# Answer: 5
# Info: reverse() - reverses the order of list:
# mm = [[1,2],[3,4],[5,6]]
# mm.reverse()
# print(mm)   Output: [[5, 6], [3, 4], [1, 2]]

# 8. Tuples are said to be heterogeneous. What does this mean?
# Answer: Mixed type objects can be stored into a single tuple

# 9. What would the following program output?
lst = [1,2,3]
tup = ("A list:", lst)
tup[1][0] = 4
print (lst[0])
# Answer: 4
# Info: Notice that, if an item of a tuple is mutable, the content of that mutable item can be changed inside the tuple.

# 10. What would be the value assigned into variable ct after the following program is executed?
lst = [(1,2),(3,2),(5,2)]
ct = lst.count(2)
print(ct)
# Answer: 0
# Info: in lst.count() need to use (1,2) for example, not separated 2. As it is a tuple's object.
# For example, in this code:
lst = [(1,2),(3,2),(5,2)]
ct = lst.count((1,2))
print(ct)         # Output: 1