#write a program that takes a string and returns True if it is a palindrome, False otherwise.
def is_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False
result1 = is_palindrome("amma")
result2 = is_palindrome("janani")
print(result1, result2)

