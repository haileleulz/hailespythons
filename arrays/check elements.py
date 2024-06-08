#  Write a function that checks if an array contains a specified element.

def check_element(numb, value):
    numb = list(map(int,numb.split(",")))
    is_present = False
    for x in numb:
        if x == value:
            is_present = True
            break
    return is_present


user_input = input("please input a number : ")
check = int(input("please input what you want to check : "))
y = check_element(user_input, check)
print(y)