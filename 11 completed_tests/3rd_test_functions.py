# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd.
# lesser_2evens(2,4) --> 2
# lesser_2evens(2,5) --> 5
def lesser_2evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)
result = lesser_2evens(2, 5)
print(result)                           # 5

# Write a function takes a two-word string and returns True if both words begin with same letter.
def same_letters(text):
    lst = text.split()
    if lst[0][0] == lst[1][0]:
        return True
    else:
        return False
result = same_letters("cool cat")
result1 = same_letters("cool dog")
print(result)                           # True
print(result1)                          # False

# Given two integers, return True if the sum of the integers is 20, 
# *or* if one of the integers is 20. If not, return False.
# check_twenty(20,10)   --> True
# check_twenty(12,8)    --> True
# check_twenty(2,3)     --> False
def check_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False
result1 = check_twenty(20,10)
result2 = check_twenty(12,8)
result3 = check_twenty(2,3)
print(result1)                          # True
print(result2)                          # True
print(result3)                          # False

# Section 1
# Write a function that capitalizes the first and fourth letters of a name:
# old_capitalize_1_4('professor') --> ProFessor

# 'professor'.capitalize() returns 'Professor'
def capitalize_1_4(name):
    new_name = ""
    for letter in range(0, len(name)):
        if letter == 0 or letter == 3:
            new_name += name[letter].capitalize()
            pass
        else:
            new_name += name[letter]          
            pass
    return new_name
name = "professor"
name = capitalize_1_4(name)
print(name)

# Given a sentence, return a sentence with the words reversed
# reversed_string('I am happy') --> 'happy am I'
# The .join() method allows us to join together strings in a list with some connector string:
# "--".join(['Hello','world'])       --> "Hello--world"

def reversed_string(text):
    lst = text.split()
    lst.reverse()
    new_text = " ".join(lst)
    return new_text

text = "I am happy"
text = reversed_string(text)
print(text)                             # happy am I

# Given an integer num, return True if num is within 10 of either 100 or 200:
# how_close(90)  --> True
# how_close(104) --> True
# how_close(150) --> False
# how_close(209) --> True

# abs(num) returns the absolute value of a number
def how_close(num):
    if abs(100 - num) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False
num = int(input("Enter any integer: "))
result = how_close(num)
print(result)

# Section 2
# Given a list of integers, return True if the array contains a 4 next to a 4 somewhere.
# check_44([1, 4, 4])     → True
# check_44([1, 4, 1, 4])  → False
# check_44([4, 1, 4])     → False
def check_44(lst):
    for num in range(0, len(lst) - 1):
        if lst[num] == 4:
            if lst[num + 1] == 4:
                return True
        else:
            pass
    return False
    
lst = [1, 2, 2, 2, 5, 6, 7, 8, 9, 4]
result = check_44(lst)
print(result)                           # False

# Given a string, return a string where for every character in the original there are three characters.
# triple_char('Mississippi') --> 'MMMiiissssssiiippppppiii'
def triple_char(text):
    new_text = ''
    for letter in range(0, len(text)):
        new_text += text[letter]*3
    return new_text
text = "Mississippi"
result = triple_char(text)
print(result)                           # MMMiiissssssiiissssssiiippppppiii

# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'OOPS'
# game21(5,6,7)      --> 18
# game21(9,9,9)      --> 'OOPS'
# game21(9,9,11)     --> 19

def game21(num1, num2, num3):
    lst = [num1, num2, num3]
    x = sum(lst)
    if x <= 21:
        return sum(lst)
    if x > 21 and 11 in lst:
        x = sum(lst) - 10
        if x > 21:
            return 'OOPS'
        elif x <= 21:
            return x
    elif x > 21:
        return 'OOPS'
res1 = game21(5,6,7)
res2 = game21(9,9,9)
res3 = game21(9,9,11)
print(res1)                             # 18
print(res2)                             # OOPS
print(res3)                             # 19

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
# noneed_69([1, 3, 5])          --> 9
# noneed_69([4, 5, 6, 7, 8, 9]) --> 9
# noneed_69([2, 1, 6, 9, 11])   --> 14
def noneed_69(numbers):
    new_lst = []
    for num in range(0, len(numbers)):
        if numbers[num] in [6, 7, 8, 9]:
            pass
        elif len(numbers) == 0:
            return 0
        else:
            new_lst.append(numbers[num])
    return sum(new_lst)
out1 = noneed_69([1, 3, 5])
out2 = noneed_69([4, 5, 6, 7, 8, 9])
out3 = noneed_69([2, 1, 6, 9, 11])
out4 = noneed_69([])
print(out1)
print(out2)
print(out3)
print(out4)

# Section 3
# Write a function that takes in a list of integers and returns True if it contains 007 in order:
# bond_007([1,2,4,0,0,7,5])     --> True
# bond_007([1,0,2,4,0,5,7])     --> True
# bond_007([1,7,2,0,4,5,0])     --> False

def lst_check(lst):
    new_lst = []
    for num in range(0, len(lst)):
        if lst[num] == 0 or lst[num] == 7:
            new_lst.append(lst[num])
        else:
            pass
    return new_lst

def bond_007(check):
    if len(check) < 3:
        return False
    for n in range(0, len(check)-2):
        if check[n] == 0:
            if check[n+1] == 0:
                if check[n+2] == 7:
                    return True
        else:
            pass
    return False
lst = [1,2,7,8,0,0,1,0,0,0] 
check = lst_check(lst)
result = bond_007(check)
print(result)                           # Output: False

# Write a function that returns the number of prime numbers that exist up to and including a given number:
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.
def prime_numbers(num):
    lst = [number for number in range(2, num+1)]
    lst2 = [number for number in range(2,num+1)]
    for x in lst:
        for y in lst2:
            if x == y:
                if y % x != 0:
                    pass
            elif y % x == 0:
                lst2.remove(y)
    return lst2

def count_primes(prime_nums_lst):
    return len(prime_nums_lst)

num = 100
prime_nums_lst = prime_numbers(num)
amount_of_primes = count_primes(prime_nums_lst)
print(amount_of_primes)                 # 25
print(prime_nums_lst)                   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# big_letter('a')
# out:   *  
#       * *
#      *****
#      *   *
#      *   *
def a():
    print(2 * " " + "*")
    print(" " + "*" + " " + "*" + " ")
    print(5 * "*")
    print("*" + 3 * " " + "*")
    print("*" + 3 * " " + "*")

def b():
    print(4 * "*" + " ")
    print("*" + 3 * " " + "*")
    print(4 * "*" + " ")
    print("*" + 3 * " " + "*")
    print(4 * "*" + " ")

def c():
    print(" " + 4 * "*")
    print("*")
    print("*")
    print("*")
    print(" " + 4 * "*")

def d():
    print(4 * "*" + " ")
    print("*" + 3 * " " + "*" )
    print("*" + 3 * " " + "*" )
    print("*" + 3 * " " + "*" )
    print(4 * "*" + " ")

def e():
    print(5 * "*")
    print("*" + 4 * " ")
    print(5 * "*")
    print("*" + 4 * " ")
    print(5 * "*")

def big_letter(letter):
    my_dictionary = {'a':a,'b':b,'c':c,'d':d,'e':e}
    if letter in ['a','b','c','d','e']:
        return my_dictionary.get(letter)()
    else:
        print("At the moment, only the letters 'a','b','c','d','e' can be shown.")

letter = 'd'
result = big_letter(letter)