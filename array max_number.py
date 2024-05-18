# Write a Python function to find the maximum number in a given array.

def max_number(numb):
    numb = list(map(int, numb.split(",")))
    max_max = numb[0]
    for x in numb:
        if x > max_max:
            max_max = x
    return max_max


list1 = input("please input a number : ")
y = max_number(list1)
print(y)