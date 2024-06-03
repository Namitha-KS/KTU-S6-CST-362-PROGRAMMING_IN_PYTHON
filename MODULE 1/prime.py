# number = int(input("ENTER NUMBER : "))
# i = 2
# flag = True
# while i<number:
#     if (number%i==0):
#         flag = False
#         break
#     i+=i
# if(flag==True):
#     print("PRIME")
# else:
#     print("NOT PRIME")

def print_prime_factors(n):
    prime_factors = []
    
    if n <= 1:
        return prime_factors
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    sqrt = int(n ** 0.5)
    for i in range(3, sqrt + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    print(f"Prime factors of {n} are: {prime_factors}")


print_prime_factors(12)  # Prime factors of 12 are: [2, 2, 3]
print_prime_factors(100)  # Prime factors of 100 are: [2, 2, 5, 5]
print_prime_factors(17)  # Prime factors of 17 are: [17]
print_prime_factors(-4)  # Prime factors of -4 are: []