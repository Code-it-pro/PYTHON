def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        fact = n * factorial(n-1)
    return fact

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f'Factorial of {n}: {factorial(n)} ')