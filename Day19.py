def armstrong_number(num):
    original_number = num
    num_digits = len(str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit ** num_digits
        num //= 10

    return sum == original_number

number = int(input("Enter a number: "))

if armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
