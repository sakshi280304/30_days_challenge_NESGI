def string_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

user_input = input("Enter a string: ")

length = string_length(user_input)
print(f"The length of the string is: {length}")
