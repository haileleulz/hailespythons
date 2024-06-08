# Write a Python script to find the second-largest number in an array.

def second_largest(numb):
    if len(numb) < 2:
        return "invalid input"
    numb = list(map(int,numb.split(",")))
    numb.sort()
    second_max = numb[-2]
    return second_max


user_input = input("please input a number : ")
x = second_largest(user_input)
print(x)