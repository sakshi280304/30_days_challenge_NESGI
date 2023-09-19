def find_maximum(a, b):
    maximum = (a > b) * a + (a <= b) * b
    return maximum

def find_minimum(a, b):
    minimum = (a < b) * a + (a >= b) * b
    return minimum

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

maximum = find_maximum(num1, num2)
minimum = find_minimum(num1, num2)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

