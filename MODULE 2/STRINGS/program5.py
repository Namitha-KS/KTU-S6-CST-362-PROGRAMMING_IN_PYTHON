# Write a program to slice the string into two separate strings; one with all the characters in the odd indices and one with all characters in even indices.

string = input()
string1 = " "
string2 = " "
for ch in string:
    if string.index(ch)%2==0:
        string1 += ch
    else:
        string2 += ch
print(string1)
print(string2)