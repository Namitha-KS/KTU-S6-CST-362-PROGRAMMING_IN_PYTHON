# Write a program to remove characters at odd index positions from a string.

string = input()
string1 = ''
for ch in string:
    if string.index(ch) % 2 == 0:
        string1 += ch
print(string1)