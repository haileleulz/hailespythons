# Write a function `sum_of_digits` that takes a number and returns the sum of its digits.

def sum_of_digits(numb):
    numb = numb.split(",")
    sum1 = 0
    for x in numb:
        sum1 += int(x)
    return sum1


user_input = input("Please input a number : ")
y = sum_of_digits(user_input)
print(y)