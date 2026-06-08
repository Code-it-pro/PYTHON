def pattern(n):
    if n==0:
        return ""
    else:
        print("*" * n)
        n -=1
    pattern(n)

n = int(input("Enter a number: "))
pattern(n)