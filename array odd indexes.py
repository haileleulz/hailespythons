#  Write a program that prints only the elements at odd indices in an array.

def odd_index(numb):
    numb = list(map(int,numb.split(",")))
    odd_ind = []
    for x in range(1,len(numb) + 1, 2):
        odd_ind.append(x)
    return odd_ind


user_input = input("please input a list : ")
y = odd_index(user_input)
print(y)