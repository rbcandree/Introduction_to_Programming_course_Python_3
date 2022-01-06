"""
Example about basic list initialization and setting the values of cells. 
Note, that the indexing begins at zero, so the last item in a list is at the index [len(list) - 1].
"""
def main():
    a = [0] * 3         # Array a is created. The size of array is 3. #001 = [0, 0, 0]
    output(a)           # Method call output - now executes line 13, as it's called function "output(n)"
    a[0] = 1            # The value of cell 0 in array a is changed to 1. a = [1, 0, 0]
    a[1] = a[0] * 4 + 2 # The value of cell 1 in array a is changed to 6. (1 * 4 + 2). a = [1, 6, 0]
    a[2] = 8 - a[a[0]]  # The value of cell 2 in array a is changed to 2. a[2] = 8 - 6 --> a[2] = 2 --> a = [1, 6, 2]
    output(a)           # Method call output -  now executes line 13, as it's called by function "output(n)"

def output(n):                  # Initialising variable n with value a = [0, 0, 0]
                                # Initialising variable n with value a = [1, 6, 2]
    for i in range(0,len(n),1): # Initialising variable i with value 0. For loop rotates. Condition ( i<n.length) --> (0 < 3 ) is True. Execution continues inside the block.
                                # Initialising variable i with value 0. For loop rotates. Condition ( i<n.length) --> (0 < 3 ) is True. Execution continues inside the block.
                                # The value of variable i is changed to 1.For loop rotates. Condition ( i<n.length) --> (1 < 3 ) is True. Execution continues inside the block.
                                # The value of variable i is changed to 1. Condition ( i<n.length) --> (1 < 3 ) is True. Execution continues inside the block.
                                # The value of variable i is changed to 2.For loop rotates. Condition ( i<n.length) --> (2 < 3 ) is True. Execution continues inside the block.
                                # The value of variable i is changed to 2. Condition ( i<n.length) --> (1 < 3 ) is True. Execution continues inside the block.
                                # The value of variable i is changed to 3.For loop rotates. Condition ( i<n.length) --> (3 < 3 ) is False. The block is not executed.
                                # The value of variable i is changed to 3. Condition ( i<n.length) --> (3 < 3 ) is False. The block is not executed.
        print (n[i]) # Output 0.
                     # Output 0.
                     # Output 0.
                        # Output 1.
                        # Output 6.
                        # Output 2.

# Function ends. Returning value to variable a (line 7). Next line is line 8 will be executed.
"""
Questions:
1. Which of the following indexes are valid when referencing cells in list a?
    a = [0] * 3
Answer: Indexes 0...2
Remember, that the indexing in arrays always begins at zero. Hence, a list a has items at indexes
    m[0] .... m[m.length - 1]

    An index of a list is valid only if that index can be accessed from the list, without causing some error.
Generally, this means that the index must be a whole number, and it must be less than the length of the list, 
because any index greater than the list length is out of range.
    Each element in a list has an index that specifies its position in the list. Indexing starts at 0, so the
index of the first element is 0, the index of the second element is 1, and so forth. The index of the last element 
in a list is 1 less than the number of elements in the list.
    For example, the following statement creates a list with 4 elements:
my_list = [10, 20, 30, 40]
    The indexes of the elements in this list are 0, 1, 2, and 3. We can print the elements of the list with the following statement:
print(my_list[0], my_list[1], my_list[2], my_list[3])

2.  Which is the correct value of len(n)?
    for i in range(0,len(n),1):
Answer: 3

3. What does this line output?:
    print (n[i])
Answer: integer 0 three times.

4. Insert correct value to list a.
    a[1] = a[0] * 4 + 2
Answer: a = [1, 6, 0]
a = [0, 0, 0] --> [0] = 1 --> a = [1, 0, 0] --> a[1] = a[0] * 4 + 2 --> a = [1, 6, 0]

5. Insert corrct value to list a.
    a[2] = 8 - a[a[0]]
Answer: a = [1, 6, 2]
a = [1, 6, 0] --> a[2] = 8 - a[1] --> a[2] = 8 - 6 --> a[2] = 2 --> a = [1, 6, 2]

6. What does this line output?
    print (n[i]) (4nd time)
Answer: 1. (As, n[0] from n = [1, 6, 2] is 1)

7. What does this line output?
    print (n[i]) (6th time)
Answer: . (As, n[2] from n = [1, 6, 2] is 2)
"""