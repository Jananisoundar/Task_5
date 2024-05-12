#write a program that takes a string and returns the most frequent chracters in it.
def most_frequent_char(s):
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1

        else:
            letter_count[char] = 1
    print(letter_count)
    most_common_char = max(letter_count, key=letter_count.get)
    return most_common_char
string = "ketki"
most_common_character = most_frequent_char(string)
print("The most frequent character is:", most_common_character)
