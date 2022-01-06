# List comprehensions allow us to build out lists using a different notation. 
# It is like a one line for loop built inside of brackets:

# Grab every letter in string
mystring = 'Alabama'
lst_old = []
for letter in mystring:
    lst_old.append(letter)
print(lst_old)                                      # Output: ['A', 'l', 'a', 'b', 'a', 'm', 'a']
# Or:
lst = [x for x in 'Alabama']
print(lst)                                          # Output: ['A', 'l', 'a', 'b', 'a', 'm', 'a']


lst2 = [x*2 for x in range(11)]                     # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(lst2) 

lst3 = [x**2 for x in [x*2 for x in range(11)]]     # Output: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
print(lst3)

lst4 = [num for num in range(0, 11)]                # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst4)

lst_odd = [x for x in range(0, 16) if x % 2 == 1]   # Output: [1, 3, 5, 7, 9, 11, 13, 15]
print(lst_odd)

# Example with temperature:
celcius = [0, 7.7, 12.2, 16.5, 23.0, 28.9, 33.4]
fahrenheit = [(temp*(5/9) + 32) for temp in celcius]    # Output: [32.0, 36.27777777777778, 38.77777777777778, ..., 50.55555555555556]
f = [round(x, 1) for x in fahrenheit]
print(f)                                                # Output: [32.0, 36.3, 38.8, 41.2, 44.8, 48.1, 50.6]

lst_even = [x if x % 2 == 0 else "Odd" for x in range(0, 11)]
print(lst_even)                                         # Output: [0, 'Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]

# Other:
lst5 = []
for num_1 in [1, 2]:
    for num_2 in [100, 200, 300, 400, 500]:
        lst5.append(num_1 + num_2)
print(lst5)                                             # Output: [101, 201, 301, 401, 501, 102, 202, 302, 402, 502]

# Or:
lst5_new = [num_1 + num_2 for num_1 in [1, 2] for num_2 in [100, 200, 300, 400, 500]]
print(lst5_new)                                         # Output: [101, 201, 301, 401, 501, 102, 202, 302, 402, 502]