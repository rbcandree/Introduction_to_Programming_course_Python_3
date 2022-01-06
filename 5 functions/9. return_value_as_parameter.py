def main():
    a = 5
    #Initialising variable a with value 5.
    b = increse(a)
    #Return value 10. Initialising variable b with value 10.
    c = decrese(b)
    #Return value 5. Initialising variable c with value 5.
    d = increase(decrease(c+b))
    #Return value 10.
    #Return value 15.
    #Initialising variable d with value 15.
    print(a + " , " + b + " , " + c + " , " + d)
    #Output:    5 , 10 , 5 , 15 
    #          (5 + " , " + 10 + " , " + 5 + " , " + 15)

def increase(n):
    #Initialising variable n with value 5.
    #Initialising variable n with value 10.
    return n + 5
    #Return 10. (5 + 5)
    #Return 15. (10 + 5)

def decrease(n):
    #Initialising variable n with value 10.
    #Initialising variable n with value 15.
    return n - 5
    #Return 5. (10 - 5)
    #Return 10.(15 - 5)

"""
Questions:
1. What will be the value of variable b after the execution of function increase?
b = increse(a)
Answer: 10

2. What code line will be executed next?
def increase(n):
Answer: 
3rd line:   b = increse(a)

3. What will be the value of variable n after this code line is executed?
def decrease(n):
Answer:
10
Because:
def decrease(n):
    #Initialising variable n with value 10.
    ...
    return n - 5
    #Return 5. (10 - 5)
    ...

4. What code line will be executed next?
d = increase(decrease(a+b))
Answer:
11 line:  def decrease(n):  

5. What code line will be executed next?
d = increase(decrease(a+b))
Answer:
8 line:  def increase(n):

6. What will be the value of variable d after this return-statement is executed?
return n + 5
Answer: 15
(Returns 15. (10 + 5))
"""