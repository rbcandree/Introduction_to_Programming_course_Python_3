#Sort the items in array m to match the order after executing the following code segment:

m = [ 3, 5, 2, 1, 4, 7, 6, 8 ]
for i in range(0, 4): 
    t = m[i]
    m[i] = m[len(m) - 1 - i]
    m[len(m) - 1 - i] = t
print(m)

"""
Algorythm:
m = [ 3, 5, 2, 1, 4, 7, 6, 8 ]
for i in range(0, 4):   #range: 0, 1, 2, 3
    # i = 0
    t = m[0] #t = m[0] = 3
    m[0] = m[8 - 1 - 0] # m[0] = m[7] --> [ 3, 5, 2, 1, 4, 7, 6, 8 ] --> [ 8, 5, 2, 1, 4, 7, 6, 8 ]
    m[8 - 1 - 0] = t # m[7] = 3 (line 16: t = 3) --> [ 8, 5, 2, 1, 4, 7, 6, 8 ] --> [ 8, 5, 2, 1, 4, 7, 6, 3 ]
"""