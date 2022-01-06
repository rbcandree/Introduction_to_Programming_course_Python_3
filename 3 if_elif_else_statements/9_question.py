a = 3
b1 = a % 2 == 0
b2 = not(b1 or False)
b3 = not(b1 and b2)

x = b1 or b2 and b3
print(x)

"""
b1 and b2 and b3
b1 or not b2 or not b3
b1 and not b2 and b3
b1 or not(b2 and b3)

They are False
x = True
"""