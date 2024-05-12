#write a program to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in the string.
string = "Guvi Geeks Network Private Limited"
number_of_vowels = 0
Vowels = ""
for str in string:
    if str=='a'or str=='e'or str=='i'or str=='o' or str=='u':
         number_of_vowels = number_of_vowels +1
         Vowels += str
print("Total number of vowels in the given string:",number_of_vowels)
a = Vowels.count("a")
e = Vowels.count("e")
i = Vowels.count("i")
o = Vowels.count("o")
u = Vowels.count("u")
print("The vowels letters in the given string:", Vowels)
print("Count of a:",a, "Count of e:", e, "Count of i:" ,i ,"Count of o:", o, "Count of u:",u)
