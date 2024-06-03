n =  int(input())
sum = 0
for i in range (1,n+1):
    if(i%2==0) and (i>0):
        cube = i**3
        sum += cube
print(sum)