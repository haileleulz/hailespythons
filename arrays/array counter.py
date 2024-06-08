# Develop a Python script to count the number of occurrences of a specific
# element in an array.

def count_of_items(numb, value):
    numb = list(map(int, numb.split(",")))
    counter = 0
    for x in numb:
        if x == value:
            counter += 1
    return counter


user_input = input("please input a number : ")
key_value = int(input("please input the value : "))
y = count_of_items(user_input, key_value)
print(y)
