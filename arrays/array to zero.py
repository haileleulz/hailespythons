# Develop a function that sets all negative numbers in an array to zero
# and prints the resulting array.

def neg_to_zero(numb):
    numb = list(map(int,numb.split(",")))
    new_list = []
    for x in numb:
        if x < 0:
            x = 0
            new_list.append(x)
        else:
            new_list.append(x)
    return new_list


user_input = input("please input a list : ")
y = neg_to_zero(user_input)
print(y)
