# Write a Python program to reverse the elements of an array.

def reverse_array(numb):
    return numb[::-1]

user_input = input("please input a number : ")
x =reverse_array(user_input)
print(x)