# 1. What does the following code segment do when executed?
a = [1,2,3]
b = [4,5,6]
c = a
a = b
b = c
# Answer: WRONG       It copies the reference in a to b and c
#         CORRECT     It swaps the references stored in a and b
# Remember, that array variables hold a reference to the list. This reference can be assigned like any other variable value. 
# Info:   If we assign a variable y with a list variable x, they will refer to the same list object. 
# This can be seen with id() function, the objects have the same identity number. 
# If we now change either of x or y, the changes will appear on both lists, because they refer to the same object. 
# There are two ways to prevent this. One is that we use copy() method for the list to be copied,
# another is that we use list() constructor for the list to be copied. 
# Now the lists x and y have exactly the same content but they refer to a different object, 
# which means changes to the objects do not affect the other object.

# 2. What does the following program code segment output?
s = [ "aa", "bb", "cc" ]
r = s[2] + s[0]
print (r + s[1])
# Answer: ccaabb
# Info: Remember, that the indexing of lists always starts from a zero.

# 3. How many values does a list defined like this contain?
# my_list = ([0,1,2] + [3,4,5]) * 4
# Answer: 24
# Output --> [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
# info:   In Python, the + and * operators can be used to add and multiply lists. 
# Consider these examples:
a = [1, 2] + [3, 4]     # --> creates a list with values [1,2,3,4]
b = [1, 2] * 3          # --> creates a list with values [1,2,1,2,1,2]

# 4. Which value is assigned into my_list[1], after the following code segment is executed? 
my_list = range(1,20,3)
# Answer: 4
# Output: [1, 4, 7, 10, 13, 16, 19]
# Info: The range(start, end, step) function creates a new list with values starting from start, and going until end with a step of step. 
# Note, that if you don't need an actual list (for example in for statement), you can use the xrange function, 
# which iterates through the values simlarly, but without creating a list in memory:
for i in xrange(1,10):
   print(i)     # outputs values 1...9

# 5. What is the value of variable s after the following code segment is executed?
n = [1, 2, 3, 4, 5]
s = 0
for i in range (1, len(n)):
   s = s + n[i]
# Answer: 14
# Info: Remember that the indexing of arrays begins at zero.

# 6. How many values does the following program code segment output?
n = [1, 2, 3, 4, 5]
m = [5, 4, 3, 2, 1]
i = 0
while n[i] < m[i]:
  print (n[i] * m[i])
  i = i + 1
# Answer: 2
# Output: 5
#         8

# 7. What will the following program code output?
li = [True, False, 2 > 1.5]
print (li[0] and (li[1] or li[2]))

# Answer: True
# Info:  Remember how the logical operators work:
# a and b == True, if a == True and b == True
# a or b == True, if a == True or b == True

# 8. Which value does the item a[3] hold after the following code is executed?
b = range(1,10)
a = [x * 2 for x in b]
# Answer: 8
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18]
# Info: The for statement in expression can be used to create a new list using the values in existing list. Consider this example:
a = [1,2,3]
b = [x + 1 for x in a]  # --> b holds values [2, 3, 4]

# 9. What are the values stored in array m after the following program code segment is executed?
m = [ 10, 100, 1000 ]
n = m
n[0] = m[1] + m[2]
m[0] = m[0] + n[1]

# Answer: [1200, 100, 1000]
# info:   When two or more variables reference the same object, changing the item values applies for that same object also. 
# Consider this example:
a = [1,2,3]
b = a                   # --> reference copied
b[0] = 3
print(a[0])             # --> outputs 3

# 10. What does the following program code segment output when executed?
mx = [1, 3, 5, 2, 4, 6]
sum = 0
while mx[0] < 4:
  sum = sum + mx.pop(0)
print(sum)
# Answer: 4
# Info: Note, that in this kind of case you don't need to increase the index variable: 
# popping an item returns and removes it from the array. 
# Consider the following example, which calculates the sum of values in a list of integers:
m = range(1,20)
sum = 0
while len(m) > 0:
    sum = sum + m.pop(0)


mx = [1, 3, 5, 2, 4, 6]
sum = mx.pop(0)
print(sum)              # --> Output: 1

mx = [1, 3, 5, 2, 4, 6]
i = 0
sum = 0
while mx[0] < 4:
    sum = sum + mx.pop(0)
    print(sum)          # --> Output: 1 and on new line: 4
    i += 1