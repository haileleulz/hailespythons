# Create a Python script to swap the first and last elements of an array.

def swap_var(numb):
    numb = list(map(int, numb.split(",")))
    start = numb[0]
    end = numb[-1]
    mid = numb[1:-1]
    final = f"{end}  {', '.join(map(str, mid))}  {start}"
    return final


user_input = input("please input a number : ")
x = swap_var(user_input)
print(x)

# by using indexing

def swap_var(numb):
    numb = list(map(int, numb.split(",")))
    numb[0], numb[-1] = numb[-1], numb[0]
    return numb


user_input = input("please input a number : ")
x = swap_var(user_input)
print(x)
