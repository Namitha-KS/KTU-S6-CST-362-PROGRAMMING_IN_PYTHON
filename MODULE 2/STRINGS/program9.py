'''10.Write a Python program to check the validity of a password given by the user
The Password should satisfy the following criteria:
1. Contains at least one letter between a and z
2. Contains at least one number between 0 and 9
3. Contains at least one letter between A and Z
4. Contains at least one special character from $, #, @
5. Minimum length of password: 6'''

string = input()
u,l,d,s = 0,0,0,0
if len(string)>=6:
    for ch in string:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isdigit():
            d+=1
        elif (ch=='$') or (ch=='#') or (ch=='@'):
            s+=1
print(u,l,d,s)
if u>=1 and l>=1 and d>=1 and s>=1:
    print('Valid')
else:
    print('Invalid')