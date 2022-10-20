def linearSearch(array, m, x):

    for i in range(0, m):
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9]
x=int(input("enter value to be searched:"))
m = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
