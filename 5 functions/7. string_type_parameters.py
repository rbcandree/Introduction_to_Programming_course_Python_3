def main():
    s = "abcdefg"
    #Initialising variable s with value #001 ("abcdefg")
    s = reverse(s)
    #The value of variable s is changed to #0010 ("gfedcba")
    print(s)
    #Output: gfedcba

def reverse(r):
#Initialising variable r with value s (#001)
    k = ""
    #Initialising variable k with value #002 ("")
    for i in range(len(r) - 1, -1, -1):
    #Initialising variable i with value 6. (7 - 1) For loop rotates. Condition ( i >= 0) --> (6 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 5. For loop rotates. Condition ( i >= 0) --> (5 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 4. For loop rotates. Condition ( i >= 0) --> (4 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 3. For loop rotates. Condition ( i >= 0) --> (3 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 2. For loop rotates. Condition ( i >= 0) --> (2 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 1. For loop rotates. Condition ( i >= 0) --> (1 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 0. For loop rotates. Condition ( i >= 0) --> (0 >= 0 ) is True. Execution continues inside the block.
    #The value of variable i is changed to -1.For loop rotates. Condition ( i >= 0) --> (-1 >= 0 ) is False. The block is not executed.

        k = k + r[i]
        #The value of variable k is changed to #003 ("g"): ( + "g")
        #The value of variable k is changed to #004 ("gf"). (g + "f")
        #The value of variable k is changed to #005 ("gfe"). (gf + "e")
        #The value of variable k is changed to #006 ("gfed"). (gfe + "d")
        #The value of variable k is changed to #007 ("gfedc"). (gfed + "c")
        #The value of variable k is changed to #008 ("gfedcb"). (gfedc + "b")
        #The value of variable k is changed to #009 ("gfedcba"). (gfedcb + "a")

        return k
"""
Questions:
1. What is the best name for the following function "my reverse"?
Answer: my_reverse

2. Which of the following is a legal name for a function in Python?
Answer: myFunction3

3. What type of value this function returns?
Answer: string

4.  How many rounds will this for-loop be executed?
Answer: 7
Because: r = "abcdefg"  len(r) = 7
        for i in range(len(r) - 1, -1, -1):
        for i in range(6, -1, -1):
            1. 6 > -1
            2. 5 > -1
            3. 4 > -1
            4. 3 > -1
            5. 2 > -1
            6. 1 > -1
            7. 0 > -1
            stop -1 NOT > -1
5. What will be the value of variable k after this round is executed?
Answer: "gfedc"
6. What code line will be executed next?
    return k
Answer: 3
    Next is a 3rd line 
    Returns value k (gfedcba) to s = reverse(s) (line 3).
    The value of variable s is changed to #0010 ("gfedcba").
"""