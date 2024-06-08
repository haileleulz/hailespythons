# Create a function `find_factors` that takes an integer and returns a
# list of all its factors.

def find_factors(numb):
    factors = []
    for x in range(1, numb + 1):
        if numb % x ==0:
            factors.append(x)
    return factors


user_input = int(input("Please input a number : "))
y  = find_factors(user_input)
print(y)
