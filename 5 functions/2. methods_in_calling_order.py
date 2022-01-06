"""
Consider this main program:
a = add(multi(3));
a = a + mod(div(a + 3)) + sub(12)

Sort the method names below in the order where they are called in the program; 
the method called first should be at the top, and the method called last at the bottom.
"""

a = add(multi(3))
a = a + mod(div(a + 3)) + sub(12)

""""
Order:
1. multi
2. add
3. div
4. mod
5. sub
"""