# Write a function `count_characters` that takes a string and returns a
# dictionary with each character as a key and its count as the value.

def count_characters(numb):
    count = {}
    for x in numb:
        count[x] = count.get(x, 0) + 1
    return count


user_input = input("Please input a number : ")
y = count_characters(user_input)

for x, value in y.items():
    print(f"{x} : {value}")