"""
Write two procedures, called print_hello() and print_world().
The print_hello procedure outputs string 'Hello,' and the print_world string 'World' 
(both outputs include a new line character). 

For example, calling the procedures in order
print_hello()
print_world()
print_hello()

...would output
 
Hello
World
Hello
"""
import random

def print_hello():
    print("Hello")
    
def print_world():
    print("World")

for i in range(0,10):
  if random.randint(0,1) == 0:
    print_hello()
  else:
    print_world()