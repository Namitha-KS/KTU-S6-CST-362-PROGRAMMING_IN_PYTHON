oc = int(input("Enter the octal number: "))
dec = 0
i = 0
while oc != 0:
    dec = dec + (oc % 10) * pow(8,i)
    oc = oc // 10
    i = i+1
bi = ""
while dec != 0:
    rem = dec % 2
    dec = dec // 2
    bi = str(rem) + bi
print("binary number is:", bi)