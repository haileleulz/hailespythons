# Write a program that inserts a new element at a specified index in an array.

# def new_item(numb, valued,indexed):
#     numb = list(map(int, numb.split(",")))
#     numb.insert(index_place,add_items)
#     return numb
#
#
# user_input = input("please input a list of numbers : ")
# add_items = int(input("please input a number to add : "))
# index_place = int(input("please identify where to place them : "))
# y = new_item(user_input,add_items,index_place)
# print(y)


def add_items(numb, valued, indexed):
    numb = numb.split(",")
    result = []
    for x in range(1, indexed):
        result.append(x)
    result.append(valued)
    for y in range(indexed, 11):
        result.append(y)
    return result


user_input = input("please input a list : ")
value = int(input("please input a number : "))
indexed = int(input("please input the index : "))
z = add_items(user_input, value, indexed)
print(z)