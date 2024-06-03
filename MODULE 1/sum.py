sum = 0
number = int(input("ENTER A NUMBER : "))
while number!=0:
    sum = sum + number%10
    number = number//10
print(sum)