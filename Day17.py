def most_frequent_element(arr):
    
    frequency_table = {}

    for element in arr:
        if element in frequency_table:
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1

    most_frequent_element = None
    max_frequency = 0

    for element, frequency in frequency_table.items():
        if frequency > max_frequency:
            most_frequent_element = element
            max_frequency = frequency

    return most_frequent_element

arr = [1, 2, 2, 4, 2, 2, 2, 1, 2, 2, 4]
result = most_frequent_element(arr)
print(f"The most frequent element is: {result}")
