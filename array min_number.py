#  Write a program to find the minimum value in an array without using built-in functions.

def min_number(numb):
    numb = list(map(int,numb.split(",")))
    min_numb = numb[0]
    for x in numb:
        if x < min_numb:
            min_numb = x
    return min_numb


user_input = input("Please input a number : ")
y = min_number(user_input)
print(y)