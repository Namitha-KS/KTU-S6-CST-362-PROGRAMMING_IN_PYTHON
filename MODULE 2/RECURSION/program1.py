# 17.Write a Python program to print the factorial of a number using recursion.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n = int(input())
print(fact(n))