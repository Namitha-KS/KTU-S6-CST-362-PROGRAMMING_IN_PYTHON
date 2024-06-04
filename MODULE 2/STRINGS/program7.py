# Write a Program to converting all lowercase letters into uppercase.

import string

string = input()
string1 = ''
string2 = ''

for i in string:
    if i.islower():
        string1 += i
    elif i.isupper():
        string2 += i
print(string1.upper())
print(string2.lower())