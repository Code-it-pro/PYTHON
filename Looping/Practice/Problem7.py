n = int(input("Enter a number: "))

'''
n = 4

 123*
 12***
 1*****
 *******

n = 3

12*    *=1
1***   *=3
*****  *=5

'''

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")