# - Write a Python function that takes a two-dimensional array and prints each element in a zigzag
# (or diagonal) order starting from the top-left corner to the bottom-right corner.

def matrix_traversal(numb):
    if not numb:
        return []

    traversal = []
    rows, col = len(numb), len(numb[0])

    for d in range(rows + col - 1):
        diagonal = []
        for x in range(max(0, d - col + 1), min(rows, d + 1)):
            y = d - x
            diagonal.append(numb[x][y])
        if d % 2 == 0:
            diagonal.reverse()
        traversal.extend(diagonal)
    return traversal


matrix = [[4 * x + y + 1 for y in range(4)] for x in range(4)]
result = matrix_traversal(matrix)

for x in matrix:
    print(x)
print()
print(result)
