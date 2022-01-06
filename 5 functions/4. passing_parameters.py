def main():
    x = 3
    y = 3
    multiply(x,y)

def multiply(n,m):
    #Initialising variable n with value 3. Initialising variable m with value 3.
    s = n + "x" + m "=" + n * m
    #Initialising variable s with value: 3 + "x" + 3 + "=" + 3 * 3
    print_with_spaces(s)
    #Method call print_with_spaces: 3x3=9

def print_with_spaces(m):
#Initialising variable m with value #001 (s). #001: 3x3=9 
    for i in range(0, len(m), 1):
    #   Initialising variable i with value 0. For loop rotates. Condition ( i < m.length()) --> (0 < 5 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 1. For loop rotates. Condition ( i < m.length()) --> (1 < 5 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 2. For loop rotates. Condition ( i < m.length()) --> (2 < 5 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 3. For loop rotates. Condition ( i < m.length()) --> (3 < 5 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 4. For loop rotates. Condition ( i < m.length()) --> (4 < 5 ) is True. Execution continues inside the block.
    #The value of variable i is changed to 5. For loop rotates. Condition ( i < m.length()) --> (5 < 5 ) is False. The block is not executed.
        print(m[i], end = " ")
        #1st Output: 3. Because m = "3x3=9" --> m[0]="3"
        #2nd Output: x. Because m = "3x3=9" --> m[1]="x"
        #3rd Output: 3. Because m = "3x3=9" --> m[2]="3"
        #4th Output: =. Because m = "3x3=9" --> m[3]="="
        #5th Output: 9. Because m = "3x3=9" --> m[4]="9"    
"""
1. Which of the following are the formal parameters of procedure multiply?
    def multiply(n,m):
Answer: n and m
Description:    Initialising variable n with value 3. 
                Initialising variable m with value 3.
Because:    def main():
                x = 3
                y = 3
                multiply(x,y)
2. Which of the following is the actual parameter in the current call of procedure print_with_spaces?
    def print_with_spaces(m):
Answer: 3x3=9
3. What variables are visible in the current state of execution?
    for i in range(0, len(m), 1):
Answer: m and i
4. How many times the block of the for-loop is still executed?
    for i in range(0, len(m), 1):
Answer: 4. Total is 5, but we already executed 1 time.
5. What code line will be executed next?
Answer: 8 line: return value print_with_spaces
        8 because it is previous function, and we are coming back to previous func after finishing current function: 
        print(m[i], end = " ")
"""