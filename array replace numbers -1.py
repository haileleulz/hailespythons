# Create an array and replace every even number with the value -1.

# def replace_with_value(numb, value):
#     numb = list(map(int, numb.split(",")))
#     for x in numb:
#         print(value,end=",")
#
#
# user_input = input("please input a number : ")
# value = int(input("please input a number : "))
# x = replace_with_value(user_input,value)

def replace_even(numb, value):
    numb = numb.split(",")
    result = []
    for x in numb:
        if int(x) % 2 == 0:
            result.append(value)
        else:
            result.append(x)
    return result


user_input = input("Please input a number : ")
value = int(input("please input a number : "))
y = replace_even(user_input, value)
print(y)