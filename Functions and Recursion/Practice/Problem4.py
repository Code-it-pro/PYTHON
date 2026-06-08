def sum_natural(n):
        if n==0:
             return 0
        else:
            return n + sum_natural(n-1)

n = int(input("Enter a number: "))

if n <= 0:
    print("Enter natural number\nExiting"+"."*15)
else:
    print(f"Sum of {n} natural numbers: ", end="")
    print(sum_natural(n))