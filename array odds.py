# Create a Python function that returns a new array containing only the odd
# numbers from the original array.

def odds_from_arrays(numb):
    numb = list(map(int,numb.split(",")))
    odds = list()
    for x in numb:
        if x % 2 != 0:
            odds.append(x)
    return odds


user_input = input("please input a number : ")
y = odds_from_arrays(user_input)
print(y)