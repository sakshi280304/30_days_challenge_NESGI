def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

original_string = str(input("Enter text to write in reverse order :"))
reversed_string = reverse_string(original_string)
print(reversed_string)
