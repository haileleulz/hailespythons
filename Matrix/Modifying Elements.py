# Consider a 4x4 matrix initialized with values from 1  to 16 (inclusive).
# Write a Python function to increase every element in the even rows (0-indexed) by 5.

### The whole even rows ###
# def increase_even_rows(numb, value):
#     for x in range(len(numb)):
#         if x % 2 == 0:
#             for y in range(len(numb[x])):
#                 numb[x][y] += value
#     return numb
#
#
# matrix = [[4*x + y +1 for y in range(4)]for x in range(4)]
#
# for x in matrix:
#     print(x)
# print()
#
# value = int(input("please input a value to add : "))
# result = increase_even_rows(matrix, value)
#
# for x in matrix:
#     print(x)

### The first index ###
def increase_even_rows(numb, value):
    for x in range(0, len(numb), 2):
        numb[x][0] += value
    return numb


matrix = [[4*x + y + 1 for y in range(4)] for x in range(4)]

for x in matrix:
    print(x)

value = int(input("Please input a number : "))
result = increase_even_rows(matrix, value)

for x in matrix:
    print(x)