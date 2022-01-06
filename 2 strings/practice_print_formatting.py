# Print formatting
# We can use the .format() method to add formatted objects to printed string statements:
sentence = 'Insert another string: {}.'.format('the new string')
print(sentence)     # Output: Insert another string: the new string.

sentence1 = "My name is {}, I am {} years old".format("John", "20")
print(sentence1)    # Output: My name is John, I am 20 years old
# OR
# Another way, by using "F strings" or "formatted string literals" method:
name = "John"
age = "20"
print(f"My name is {name}, I am {age} years old.")          # Output: My name is John, I am 20 years old.

print("Same {} variable {}".format("without", "using"))     # Output: Same without variable using

#                                      0         1        2            3
print ("The {3} {0} {2} {1}.".format("are", "italians", "not", "Rolling Stones"))
# Output: The Rolling Stones are not italians.

print ("The {r} {a} {n} {au}.".format(a="are", au="australlians", n="not", r="Rolling Stones"))
# Output: The Rolling Stones are not australlians.
# Or by using "F strings" or "formatted string literals" method:
a = "are"
au = "australlians"
n = "not"
r = "Rolling Stones"
print (f"The {r} {a} {n} {au}.")    #Output: The Rolling Stones are not australlians.

# We can use %s to inject strings into our print statements. The modulo % is referred to as a "string formatting operator":
print("Just another %s of formatting." %"way")  # Output: Just another way of formatting.

# We can pass multiple items by placing them inside a tuple after the '%' operator:
print("I'm going to buy %s apples and %s watermelons." %("some","few"))   
# Output: I'm going to buy some apples and few watermelons.

# We can also pass variable names:
x = "some"
y = "few"
print("I'm going to buy %s apples and %s watermelons." %(x,y))             # Output: I'm going to buy some apples and few watermelons.

# Format conversion methods
# Two methods %s and %r convert any python object to a string using two separate methods: str() and repr(). 
# %r and repr() deliver the string representation of the object, including quotation marks and any escape characters:
print('He said his name was %s.' %'Alan')   # Output: He said his name was Alan.
print('He said his name was %r.' %'Alan')   # Output: He said his name was 'Alan'.

# The %s operator converts whatever it sees into a string, including integers and floats. 
# The %d operator converts numbers to integers first, without rounding:
print('I bought %s kilograms of fish today.' %3.75)                 # Output: I bought 3.75 kilograms of fish today.
print('I bought %d kilograms of fish today.' %3.75)                 # Output: I bought 3 kilograms of fish today.

# Multiple Formatting
print('First: %s, Second: %5.2f, Third: %r' %('hello!',3.1415,'new'))     # Output: First: hello!, Second:  3.14, Third: 'new'

#Float formatting
result = 200 / 555
print(result)                                   # Output: 0.36036036036036034
print("The result was: {}.".format(result))     # Output: The result was: 0.36036036036036034.
print("The result was: {r}.".format(r=result))  # Output: The result was: 0.36036036036036034.

#Float formatting follows "{value:width.precision f}", for example:
print("The result was: {r:1.3f}.".format(r=result))     # Output: The result was:       0.360.
print("The result was: {r:10.3f}.".format(r=result))     # Output: The result was:      0.360.