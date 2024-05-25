# Write a program that prints only the elements at odd indices in an array.

#     numb = numb.split(",")
#     result = []
#     for x in range(len(numb)):
#         if x % 2 != 1:
#             result.append(numb[x])
#     return result
#
#
# user_input = input("Please input a list: ")
# y = odd_index(user_input)
# print(y)
# def odd_index(numb):

def odd_indices(numb):
    numb = numb.split(",")
    result = []
    for x in range(int(numb[0]), int(len(numb))+1, 2):
        result.append(x)
    return result


user_input = input("please input a number : ")
y = odd_indices(user_input)
print(y)
