# Develop a program that reads 10 integers from the user, stores them in an array,
# and prints them in the same order they were entered.

numbers = []

for x in range(0,10):
    num = int(input(f"Put your first number {x + 1}: "))
    numbers.append(num)
print("The numbers are:")

for num in numbers:
    print(num,end=" ")