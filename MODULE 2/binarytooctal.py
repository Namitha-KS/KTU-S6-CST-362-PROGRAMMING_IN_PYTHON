bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
i=1
octal=0
while decimal != 0:
    octal += int(decimal % 8)*i
    decimal /= 8
    i *= 10
print("octal number is: ",octal)