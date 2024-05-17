#  Write a Python function to merge two one-dimensional arrays into a third array.

def merged_arrays(numb1,numb2):
    array1 = list(map(int, numb1.split(",")))
    array2 = list(map(int, numb2.split(",")))
    total = []
    for x in array1:
        total.append(x)
    for y in array2:
        total.append(y)
    return total


array1 = input("Please input a data : ")
array2 = input("Please input a data : ")
new = merged_arrays(array1, array2)
print(new)
