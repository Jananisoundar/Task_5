#Write a program that takes a string and returns the number of unique characters in it.
def string(string):
    Unique_characters = ""
    for str in string:
        if str not in Unique_characters:
            Unique_characters += str
    return  len(Unique_characters)
result = string("janani")
print(result)
