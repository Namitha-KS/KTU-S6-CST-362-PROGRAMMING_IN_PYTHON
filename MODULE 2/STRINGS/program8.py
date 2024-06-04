# Write a Program to reverse the first and second half of a string separately.

string = input()
l = len(string)//2
string1 = string[:l]
string2 = string[l:]
print(string1[::-1]+string2[::-1])