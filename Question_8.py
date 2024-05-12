#write a program that takes a string and returns True if it is an anagram of another string, False otherwise.
def is_anagram(string1, string2):
    if sorted (string1) == sorted (string2):
       return True
    else:
       return False
result1 = is_anagram("heart", "earth")
result2 = is_anagram("Thoorigai", "Narumugai")
print(result1, result2)
