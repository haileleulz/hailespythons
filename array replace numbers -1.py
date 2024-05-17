# Create an array and replace every even number with the value -1.

def replace_with_value(numb, value):
    numb = list(map(int, numb.split(",")))
    for x in numb:
        print(value,end=",")


user_input = input("please input a number : ")
value = int(input("please input a number : "))
x = replace_with_value(user_input,value)
