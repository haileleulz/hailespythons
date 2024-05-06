# 1.Write a program that prints a square pattern of '*' characters.The size of the square should be provided by the user.

# numbers = int(input("please input a number : "))
#
# for x in range(1,numbers +1):
#     for y in range(1,numbers +1):
#         if x == y :
#             print("*",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# 3. Print All Prime Numbers: Write a program that prints all prime numbers up to a user-specified number.
# prime_numbers = int(input("please input a number : "))

# for x in range(2,prime_numbers +1):
#     if x >1:
#         for y in range(2,x):
#             if (x % y) == 0:
#                 break
#         else:
#             print(x)

#4. Descending Order: Write a program that asks the user for a positive integer and then prints all numbers from that integer down to 1.

# positive_integer = int(input("please input a number : "))
#
# for x in range(positive_integer,0,-1):
#     print(x)

#  Sum of Odd Numbers: Write a program to calculate the sum of odd numbers from 1 to a user-specified number.
#
# numbers = int(input("please input a number : "))
# sum = 0
#
# for x in range(1,numbers +1):
#     if x % 2 != 0:      # for odd numbers
#         sum +=x
# print(sum)

# for x in range(1,numbers +1):
#     if x % 2 == 0:     # for even numbers
#         sum += x
# print(sum)

# 6. Generate ASCII Values: Write a program that prints the ASCII values of all characters from 'a' to 'z'.

# ascii_Values = []
#
# for x in range(ord("a"),ord("z")+1):
#     print(f"{chr(x)} = values:{x}")

# 7. Double Pyramid: Write a program that prints a double-sided pyramid of stars. The height of the pyramid should be specified by the user.

# height_of_pyramid = int(input("please input a number : "))
#
# for x in range(1,height_of_pyramid +1):
#     print(" " * (height_of_pyramid -x),end=" ")
#     print("*" * (2 * x -1))
# for x in range(height_of_pyramid -1,0,-1):
#     print(" " * (height_of_pyramid -x),end=" ")
#     print("*" * (2 * x -1))

# 8.Count Divisors: Write a program that asks the user for a number and then prints how many divisors that number has.

# numbers = int(input("please input a number : "))
# count_divisor = 0
#
# for x in range(1,numbers +1):
#     if numbers % x == 0:
#         count_divisor +=1
# print(count_divisor)

# 9. Repeat User Input: Write a program that repeatedly asks the user for a word and stops only when the user types "stop". After stopping, it should print all the words entered.

# all_words = []
# while True:
#     word = input("please input a word : ")
#     if word.lower() == "stop":
#         break
#     else:
#         all_words.append(word)
# for word in all_words:
#     print(word,end=" ")

# 10. Print a Checkerboard Pattern: Write a program that prints an 8x8 checkerboard pattern using alternating '#' and ' ' characters.

# numbers = int(input("please input a number : "))
#
# for x in range(1,numbers +1):
#     for y in range(1,numbers +1):
#         if (x + y) % 2 == 0:
#             print(" ",end=" ")
#         else:
#             print("#",end="")
#     print

# 11. Power Calculator: Write a program that asks the user for a base and an exponent and then calculates the power using a loop.

# base = int(input("please input a number : "))
# exponent = int(input("please input a number : "))
# power = 1
#
# for x in range(1,base):
#     power = base ** exponent
# print(power)

# 12. Print Each Word on a New Line: Write a program that asks the user for a sentence and then prints each word in the sentence on a new line.

# sentence = input("please inpur a dialogue : ")
#
# for x in sentence.split():
#     print(x)

# 13. Sum of Digits: Write a program that asks the user for a long integer and prints the sum of the digits of that number.

# long_integer = input("please input a number : ")
# sum = 0
#
# for x in long_integer:
#     sum = int(x) + sum
# print(sum)

# 15. Diamond Pattern: Use loops to print a diamond shape pattern of stars. The vertical length of the diamond should be input by the user.

# vertical_length = int(input("Please input a number : "))
#
# for x in range(1,vertical_length + 1):
#     print(" " * (vertical_length - x),end=" ")
#     print("*" * (2 * x - 1))
# for x in range(vertical_length - 1,0,-1):
#     print(" " * (vertical_length - x),end=" ")
#     print("*" * (2 * x -1))

# 16. Multiples in Reverse: Write a program that prints the multiples of 3 from 300 down to 3.

# for x in range(300,0,-3):
#     print(x)

# 17. Character Frequency: Write a simple text analyzer that asks the user for a string and counts how often each character appears.

# text_analyzer = input("please input a word to be counted : ")
# count = {}
#
# for x in text_analyzer:
#     count[x] = count.get(x,0) +1
#
# for x,y in count.items():
#     print(f"{x} {y}")

# 18. Number Guessing Game: Enhance the number guessing game to limit the number of guesses to 5.

# secret_number = 13
# guess_limit = 5
# guess_count = 0
#
# while guess_count < guess_limit:
#     guess = int(input("please input a number upto 20 : "))
#     guess_count += 1
#     if guess > 20 or guess< 1:
#         print("please input a valid number")
#     if guess == secret_number:
#         print("you are correct")
#         break
#     elif guess != secret_number:
#         print("try again")

# 20. L-Shape Pattern: Write a program that prints an 'L' shaped pattern of '*' characters where the height and width of the 'L' are specified by the user.

# height = int(input("Please input the height : "))
# width = int(input("Please input the width  : "))
#
# for x in range(height):
#     for y in range(width):
#         if y ==0 or x == height-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()