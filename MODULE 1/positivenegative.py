n = int(input("ENTER LIMIT : "))
sumpositive = 0
p = 0
sumnegative = 0
n = 0
for i in range(n):
    num = int(input())
    if (num>0):
        p+=1
        sumpositive += num
    else:
        n+=1
        sumnegative += num
print("POSITIVE SUM : ", sumpositive)
print("NEGATIVE SUM : ", sumnegative)
print("AVERAGE OF POSITIVE NUMBERS : ",sumpositive/p)
print("AVERAGE OF NEGATIVE NUMBERS : ",sumpositive/n)