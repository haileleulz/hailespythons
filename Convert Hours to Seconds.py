# Define a function `hours_to_seconds` that converts hours
# into seconds and returns the total seconds.

def hours_to_seconds(numb):
    convertor = numb * 3600
    return convertor


user_input = float(input("please input a number : "))
y = hours_to_seconds(user_input)
print(y)