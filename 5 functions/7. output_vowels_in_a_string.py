"""
Write a procedure called output_vowels(string), which gets a random string as a parameter. 
The method outputs all vowels (a, e, i, o, u, y) in the string. 
Each vowel should be outputted in its own line. 
You can assume, that all letters in the String are in lower case. 
For example, if the method is called with parameter value of "yabba dabba doo", it should output:
a
a
a
a
o
o
"""
import random
def output_vowels(string):
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y":
            print(char)
        else:
            continue
chars = "abcdeiforusy"
string = ""
for i in range(0,24):
    string += random.choice(chars)

print("The string is: " + string)
print("Vowels:")
output_vowels(string)