# How would you write a Python function to search for a given value in  a two-dimensional
# array and return True if the value exists and False otherwise? Assume the matrix
# is not sorted in any particular order.

def search_2d_arrays(numb, target):
    for x in numb:
        for y in x:
            if y == target:
                return True
    return False


matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
target = int(input("Please input a number : "))
result = search_2d_arrays(matrix, target)
print(result)