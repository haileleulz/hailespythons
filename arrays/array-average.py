#  Write a function to calculate the average of all elements in a numeric array.

def average_array(numb):
    numb = list(map(int,numb.split(",")))
    average = sum(numb) / len(numb)
    return average


user_input = input("Please input a number : ")
x = average_array(user_input)
print(x)

# without built-in functions

def average_array(numb):
    numb = list(map(int,numb.split(",")))
    total = 0
    size = len(numb)
    for x in numb:
        total += x
    average = total / size
    return average


user_input = input("please input na number : ")
y = average_array(user_input)
print(y)