# Write a function `count_words` that takes a string (representing a sentence)
# and returns the number of words in that sentence.

def count_words(numb):
    numb = numb.split()
    counter = 0
    for x in numb:
        counter += 1
    return counter


user_input = input("Please input a number : ")
y = count_words(user_input)
print(y)