decimal = int(input("Enter a decimal number: "))
if decimal == 0:
    print(0)
else:
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
    print("The binary representation is", bitString)