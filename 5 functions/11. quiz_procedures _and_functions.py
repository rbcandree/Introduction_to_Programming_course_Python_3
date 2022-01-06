
# 1. Which type of object does the following method presumably return?
def get_value(a):
    b = a * 2
    return "Value: " + str(b)
# Answer: a string

# 2. How many lines in total does the program below output when executed?
def first():
  print ("Hello!")
  second()
 
def second():
  print ("Hi!")
 
first()
second()
# Answer: 3 

# 3. Which of the following is not a syntactically valid method name in Python?
# Answer: 1stMethod
# Because: Python does not allow subprogram or variable names that start with a number.

# 4. What does the program below output when executed?
def output(c):
    print (c * 2)
 
for i in range(1,10):
    if i % 7 == 0:
        output(i)
# Answer: 14
# Because, c = i, i % 7 == 0, i = 7
# How the modulo operator (%) works: x % y returns a remainder of the division x / y.

# 5. Which of the following statements is always true about a subprogram with signature like this:
# def my_method(a, b):
# Answer: It has two formal parameters.

# 6. Which value is returned from the following function?
def mystery_function():
    sum,a = 0,0
    while a < 5:
        sum = sum + a
        if a == 2:
         return sum
        a = a + 1
# Answer: 3
# The return statement works quite similarly to break, if used inside a loop: 
# when 'return' is encountered, the Python immediately terminates the function and returns a value. 
# Note, that if there are various loops nested, return breaks out of all them (while break only exits the innermost one).

# 7. What would the following program output when executed?
def do_something(a):
  a = a + 2
a = 5
do_something(a)
print(a)
# Answer: 5
# Because: prints only value of a = 5, not a fuction result.
# The variables defined inside subprogram body are called local variables. They are only accessible inside the block they are defined in. 
# Other blocks may have similarly named variables; it's however important to remember, that they are different variables! In this case, 
# variable 'a' in the main program is different to variable 'a' in the do_something method().

# 8. How many times is the subprogram calculate called in the following program code segment:
for i in range(0,4):
    sum = sum + calculate(sum, 2)
    if i > 2:
        sum = sum + calculate(sum, sum*2)
# Answer: 4.

# 9. Consider a subprogram with the following signature line:
def is_valid(first, second):
 
# Which of the following options is NOT a valid way to call the method?
# Answer: is_valid(2, "aaa", 4*4)
# In Python, the number of the arguments in function call must match the number of the parameters in function signature line. 
# However, the types are not preset. 
# If there are limitations for argument types, they should be properly commented within the function body.

# 10. What would the following program code segment output when executed?
def output(a, b):
    if len(a) > len(b):
        print(len(a))
    else:
        print(len(b))

a = "abcd"
b = "efghi"
output(a + b, b + "jkl")
# Answer: 9