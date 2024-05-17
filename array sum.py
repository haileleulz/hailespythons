#  Write a program to find the sum of all elements in a one-dimensional array.

def sum_elements(numb):
    numb = list(map(int, numb.split(",")))
    return sum(numb)


user_input = input("please input a number : ")
total_sum = sum_elements(user_input)
print(total_sum)

# without built-in function

def sum_elements(numb):
    numb = list(map(int,numb.split(",")))
    sum1 = 0
    for x in numb:
        sum1 += x
    return sum1


user_input = input("please input a number : ")
x = sum_elements(user_input)
print(x)