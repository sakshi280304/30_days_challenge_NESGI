def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two elements"

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest

numbers = [10, 5, 20, 15, 30]
result = find_second_largest(numbers)
print(f"The second largest number is: {result}")
