"""
By using the given codelines, construct a function that calculates and 
returns the number of positive items in the given list.
"""
lst = [1, -5, 2, -10, 3, -15]
def count_positive_items(lst):
    n = 0
    for item in lst:
        if item > 0:
            n = n + 1
    return n