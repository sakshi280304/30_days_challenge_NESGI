def second_largest(arr):
    arr.sort()
    if len(arr) < 2:
        return "Array is too small"
    return arr[-2]

array = [12, 34, 10, 896, 40]
second_largest = second_largest(array)
print("The second largest number in the array is:", second_largest)
