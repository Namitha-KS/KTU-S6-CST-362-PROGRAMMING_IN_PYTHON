import math
a = int(input("ENTER COEFFICIENT OF X^2 : "))
b = int(input("ENTER COEFFICIENT OF X : "))
c = int(input("ENTER CONSTANT : "))

if a==0:
    print("NOT A QUADRATIC EQUATION. ROOT IS ", -c/b)
else:
    root1 = float((-b+math.sqrt(b*b-(4*a*c)))/(2*a))
    root2 = float((-b-math.sqrt(b*b-(4*a*c)))/(2*a))
    print(root1)
    print(root2)