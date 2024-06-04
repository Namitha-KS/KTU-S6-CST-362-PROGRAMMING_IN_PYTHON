# Write a program to replace all the spaces in the input string with * or if no spaces found, put $ at the start and end of the string.

string = input()

flag = 0

for ch in string:
    if ch==' ':
        print(string.replace(' ',"*"))
        flag = 1
        break
        
if flag==0:
    print('$'+string+'$')