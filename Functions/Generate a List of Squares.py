# Define a function `list_of_squares` that takes an integer `n` and returns a list
# of the squares of all integers from 1 to `n`.

def list_of_squares(numb):
    squares_of_numbers = []
    for x in range(1, numb + 1):
        square = x **2
        squares_of_numbers.append(square)
    return squares_of_numbers


user_input = int(input("Please input a number : "))
y = list_of_squares(user_input)
print(y)