def even(number):
    return (number & 1) == 0

input_number = int(input("Enter an integer: "))

if even(input_number):
    print(f"{input_number} is an even number.")
else:
    print(f"{input_number} is an odd number.")
