# Write a program to remove all vowel characters from a string.

string = input()
vowels = "AEIOUaeiou"
string1 = ''
for ch in string:
    if ch not in vowels:
        string1 += ch
print(string1)