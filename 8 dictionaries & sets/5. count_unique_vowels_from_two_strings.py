"""
Construct a function that receives two strings as arguments. 
The function calculates and returns the total number of unique vowels in the two strings.
"""
string1 = "hey"
string2 = "bay"

def count_unique_vowels(string1, string2):
    chars = set()
    strings_combined = string1 + string2
    for c in strings_combined:
        if c in "aeiou":
            chars.add(c)
    return len(chars)

print(count_unique_vowels(string1, string2))