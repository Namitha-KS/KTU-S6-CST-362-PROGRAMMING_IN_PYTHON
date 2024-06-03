sum = 0
n = int(input("ENTER LIMIT : "))
for i in range (n):
    num = int(input())
    if(num%2 == 0):
        sum = sum+num
print(sum)