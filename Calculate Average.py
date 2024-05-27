# Create a function `average` that takes a list of numbers and returns the average of those numbers.

def calculate_average(numb):
    numb = numb.split(",")
    sum1 = 0
    for x in numb:
        sum1 += int(x)
    average = sum1 / len(numb)
    return average


user_input = input("Please input a number : ")
y = calculate_average(user_input)
print(y)