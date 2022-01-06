def say_hello(name):
    print(f"Hello, {name}!")
say_hello(input("What is your name?"))              # What is your name?Jack
                                                    # Hello, Jack!

def say_hello1(name = 'Inna'):
    print(f"Hello, {name}!")
say_hello1()                                        # Hello, Inna!

def divide_func(n1, n2):
    return n1//n2
result = divide_func(100, 25)
print(result)                                       # Output: 4

# Logic with Python Functions
def even_check(number):
    return number % 2 == 0
result = even_check(3)                              
print(result)                                       # Output: False

# Return True, if any number is even inside a list
def even_check_lst(lst):
    for x in lst:
        if x % 2 == 0:
            return True
        else:
            pass
lst = [1, 3, 5]
result = even_check_lst(lst)
print(result)                                       # Output: None

result1 = even_check_lst([1, 2, 3])
print(result1)                                      # Output: True
# BUT
def even_check_lst1(lst):
    for x in lst:
        if x % 2 == 0:
            return True
        else:
            pass                                    # Don't do anything
    return False
lst = [1, 3, 5]
result = even_check_lst1(lst)
print(result)                                       # Output: False

result1 = even_check_lst1([1, 2, 3])
print(result1)                                      # Output: True

# Return True, if all numbers is even inside a list
def even_check_lst1(lst):
    for x in lst:
        if x % 2 == 0:
            pass
        else:
            return False
    return True
lst = [2, 4, 6, 7, 8]
result = even_check_lst1(lst)
print(result)                                       # Output: False

result1 = even_check_lst1([2, 4, 6, 8])
print(result1)                                      # Output: True

# Return all even numbers in a list
def even_all(lst):
    # placeholder variables
    even_lst = []
    for x in lst:
        if x % 2 == 0:
            even_lst.append(x)
        else:
            pass
    return even_lst
lst = [1, 2, 3, 4, 5, 6]
even_lst = even_all(lst)
print(even_lst)                                     # Output: [2, 4, 6]