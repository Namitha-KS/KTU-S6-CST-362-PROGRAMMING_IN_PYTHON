# Write a program to remove all occurrence of a substring from a string.

string = input()
substring = input()

if substring in string:
    string = string.replace(substring, "")
    
print(string)