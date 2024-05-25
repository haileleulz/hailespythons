# Write a Python program to create a 2x3 array initialized with zeros.
# How can you access the element at the second row and third column?

def initial_access(numb):
    return numb


matrix = [[0 for y in range(3)] for x in range(2)]
result = initial_access(matrix)
for x in result:
    print(x)

print(matrix[1][2])