# Use 'for', .split(), and if to create a Statement that will print out words that start with 't':
st = 'Print only the words that start with t in this sentence'
lst = st.split()
for word in lst:
    if word[0] == 't':
        print(word)

# Or method 2 with capital T:
st = 'Tom, print only the words that start with t in this sentence'
st = st.replace(',' , '')
lst = st.split()
for word in lst:
    if word[0].lower() == 't':     # .lower() method
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11):
    if num % 2 == 0:
        print(num)
# Or:
for num in range(0, 11, 2):
    print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list1 = [num for num in range(1, 51) if num % 3 == 0]
print(list1)

# Go through the string below and if the length of a word is even print "even!"
# with using 'for loop':
st = 'Print every word in this sentence that has an even number of letters'
list2 = st.split()
for word in list2:                 # or: for word in st.split()
    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)
    
# Or with while loop:
st = 'Print every word in this sentence that has an even number of letters'
list1 = st.split()
index_count = 0
while index_count < len(list1):
    word = list1[index_count] 
    if len(word) % 2 == 0:
        print('even!')
        index_count += 1
    else:
        print(word)
        index_count += 1

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
list3 = list(range(1, 101))          
for num in list3:                   # or just:  for num in range(1, 101):     
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
st_list = st.split()
lst = [x[0] for x in st_list]
print(lst)

# Or with 'for loop':
st = 'Create a list of the first letters of every word in this string'
st_list = st.split()
new_list = []
counter = 0
for word in st_list:
    new_list.append(st_list[counter][0])
    counter += 1
print(new_list)

# Or another method:
st = 'Create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print(lst)