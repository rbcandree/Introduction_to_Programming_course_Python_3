"""
Construct a function smallest_item that finds and returns the smallest item from the matrix received as an argument.
"""
matrix =    [[1, 2, 3,4],
            [5, 6, -7, 8],
            [9, 10, 11, 12]]
def smallest_item(matrix):
    smallest = matrix[0][0]
    for row in matrix:
        for item in row:
            if item < smallest:
                smallest = item
    return smallest
print(smallest_item(matrix))