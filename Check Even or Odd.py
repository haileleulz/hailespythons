# Write a function `is_even_or_odd` that takes a number and returns "Even" if
# the number is even, and "Odd" if the number is odd.

def is_even_or_odd(numb):
    if numb % 2 == 0:
        return "number is even"
    else:
        return "number is odd"


user_input = int(input("Please input a number : "))
y = is_even_or_odd(user_input)
print(y)