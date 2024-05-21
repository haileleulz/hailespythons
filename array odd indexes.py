# Write a program that prints only the elements at odd indices in an array.

def odd_index(numb):
    numb = numb.split(",")
    result = []
    for x in range(len(numb)):
        if x % 2 != 1:
            result.append(numb[x])
    return result


user_input = input("Please input a list: ")
y = odd_index(user_input)
print(y)
