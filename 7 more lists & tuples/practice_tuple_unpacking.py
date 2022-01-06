# Tuple unpacking:

list1 = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for (x,y) in list1:
    print(x)                    
    print(y)                    # Output: 1
#                                         2
#                                         3
#                                         4
#                                         5
#                                         6
#                                         7
#                                         8
#                                         9
#                                         10

# Or:
list1 = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for x,y in list1:                    
    print(y)                    # Output: 2
#                                         4
#                                         6
#                                         8
#                                         10