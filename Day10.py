def find_missing_and_repeating(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    expected_square_sum = sum(i ** 2 for i in range(1, n + 1))

    actual_sum = sum(nums)
    actual_square_sum = sum(x ** 2 for x in nums)

    final_sum = expected_sum - actual_sum
    square_sum = expected_square_sum - actual_square_sum

    x_plus_y = square_sum // final_sum
    x = (final_sum + x_plus_y) // 2
    y = x_plus_y - x

    return x, y

array = [3, 1, 3]
repeating, missing = find_missing_and_repeating(array)
print(f"Missing number: {repeating}, Repeating number: {missing}")
