"""
The following program has three procedures defined: 

draw_small(), draw_medium() and draw_large()

which draw small, medium or large line, respectively.
Your job is to output a diamond similar to one below by calling the procedure in correct order:

  *
 ***
*****
 ***
  *
"""
import random

def draw_small():
    print((base * 2) * " " + base * "*")
    
def draw_medium():
    print(base * " " + (base * 3) * "*")
    
def draw_large():
    print ((base * 5) * "*")
    
def test():
    draw_small()
    draw_medium()
    draw_large()
    draw_medium()
    draw_small()

for i in range(5):
    base = random.randint(1,5)
    test()
    print()