# Define a function `min_and_max` that takes a list of numbers and returns
# a tuple containing the minimum and maximum numbers in the list.

def min_and_max(numb):
    numb = numb.split(",")
    max_number = int(numb[0])
    min_number = int(numb[0])
    for x in numb:
        x = int(x)
        if x > max_number:
            max_number = x
        elif x < min_number:
            min_number = x
    return max_number, min_number


user_input = input("Please input a list of numbers : ")
y = min_and_max(user_input)
print(f" maximum and minimum numbers are {y} respectively")