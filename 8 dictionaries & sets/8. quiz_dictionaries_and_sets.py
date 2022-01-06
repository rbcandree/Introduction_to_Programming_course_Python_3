# 1. Dictionary d is initialized with the following statement:
d = { 0: 1.0, 1: 2.0, 3: 4.5 }
# What is the index of the first item in d?
# Answer: There is no first item, dictionary is not ordered.

# 2. What method can be used to iterate through both, keys and values of a dictionary with a single loop?
# Answer: items.

# 3. What value will be stored into variable s after the following program is executed?
s = 0
d = {True: 10, False: 20}
s = d[s > 0]
# Answer: 20

# 4. What objects can be used as dictionary's keys?
# Answer: All immutable objects.

# 5. Which of the following is the correct way to access all values stored in dictionary d?
# Answer: 
d.keys()

# 6. What will the following program output when executed?
d = {10: 1, 20: 2, 30: 3}
s = 0
for i in d:
  s += i
print (s)
# Answer: 60

# 7. Which of the following is the correct way to initialize a new set using values stored in list my_list?
# Answer:
s = set(my_list)

# 8. How many items there are in the set st after the following program code is executed?
l = [0,1,2,0,1,0,1,2,3]
st = set(l)
# Answer: 4
# Info:         print(st) --> {0, 1, 2, 3}

# 9. How many items are there in dictionary d and in list li after the following program code is executed?
d = {1: 1, 2:2, 3:3, 0:0, 4:4}
li = list(d.keys())
for i in range(2):
    li.pop()
# Answer: 5 and 3
# Info:         print(d)    --> {1: 1, 2: 2, 3: 3, 0: 0, 4: 4}
#               print(li)   --> [1, 2, 3]

# 10. What would the following program output when executed?
s1 = set(range(4))
s2 = set(range(2,6))
s1 = s1.union(s2)
print (sum(s1))
# Answer: 15
# Info:   s1 = {0, 1, 2, 3}
#         s2 = {2, 3, 4, 5}
#         s1 = s1.union(s2) --> {0, 1, 2, 3, 4, 5}
# The union() method returns a set that contains all items from the original set, and all items from the specified set(s).