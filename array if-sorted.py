# Develop a program that checks if an array is sorted in ascending order
def if_array_sorted(numb):
    is_sorted = True
    if not numb:
        is_sorted = False
    else:
        numb1 = numb[0]
        for x in numb:
            if x < numb1:
                is_sorted = False
                break
            numb1 = x
    return is_sorted


user_input = input("please input a number : ")
x = if_array_sorted(list(map(int, user_input.split(","))))
print(x)