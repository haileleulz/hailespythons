# Create a Python program that removes all occurrences of a specified element from an array.

# def remove_dup(numb, removable_numb):
#     numb = list(map(int, numb.split(",")))
#     unique_list = list()
#     for x in numb:
#         if x == removable_numb:
#             continue
#         else:
#             unique_list.append(x)
#     return unique_list
#
#
# user_input = input("please input a list : ")
# removable_numb = int(input("please input to remove : "))
# y = remove_dup(user_input,removable_numb)
# print(y)

def count_item(numb, value):
    result = []
    for x in numb:
        if x == value:
            continue
        else:
            result.append(x)
    return result


user_input = input("Please input a number : ")
value = input("please input a number : ")
y = count_item(user_input, value)
print(y)
