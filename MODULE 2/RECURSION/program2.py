# 18.Write a Python program to print n‟th Fibonacci number using recursion.

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


# n = int(input())
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))