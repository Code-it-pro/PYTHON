n = int(input("Enter a number: "))

'''

n = 3

***
* *
* *
* *
***

'''


# print("*" * n )

# for i in range(1, n+1):
#     for i in range(1, n+1):
#         if(i == 1 or i == n):
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print("")

    
# print("*" * n)

for i in range(1, n+1):
    if(i==1 or i==n):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*")
print("")