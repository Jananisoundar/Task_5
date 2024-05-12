#write a progarm that takes two strings and return the longest common substring between them.
def longest_common_substring(str1, str2):

    longest_substring = ""
    for i in range(len(str1)):

        for j in range(i + 1, len(str1) + 1):

            if str1[i:j] in str2 and len(str1[i:j]) > len(longest_substring):
                longest_substring = str1[i:j]

    return longest_substring
result = longest_common_substring("God is great", "God is always great")
print(result)






