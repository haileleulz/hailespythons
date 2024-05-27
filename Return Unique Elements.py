# Create a function `unique_elements` that takes a list and returns a new list
# containing only the unique elements from the original list.

def unique_elements(numb):
    numb = numb.split(",")
    unique = []
    for x in numb:
        if x not in unique:
            unique.append(x)
    return unique


user_input = input("Please input a number : ")
y = unique_elements(user_input)
print(y)