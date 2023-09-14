def palindrome(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    if string == reversed_string:
        return True
    else:
        return False

string = str(input("Enter a string : "))
if palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
