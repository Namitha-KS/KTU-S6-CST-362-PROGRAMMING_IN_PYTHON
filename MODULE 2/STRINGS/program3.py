# Write a python script for palindrome checking without reversing the string.

string = input()

if string == string[::-1]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
    
# with loop

beg = 0
end = len(string)-1

while beg<end:
    if string[beg] != string[end]:
        print("NOT PALINDROME")
        break
    beg += 1    
    end -= 1
else:
    print("PALINDROME")