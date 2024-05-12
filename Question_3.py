#Write a program that takes a string and returns a new string with all the vowels removed.
def string_with_vowels(string):
    Vowles_removed_string = ""
    for str in string:
        if str not in "aeiouAEIOU":
            Vowles_removed_string += str
    return  Vowles_removed_string
result = string_with_vowels("janani")
print(result)
