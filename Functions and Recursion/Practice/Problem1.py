def maximum(count):
    l1=[]
    for i in range(count):
        l1.append(int(input("Enter a number: ")))
    
    print(f"your numbers: \n{l1}")
    maxval = max(l1)
    return maxval

count = int(input("Enter no. of numbers you need average for : "))

print(f'max value = {maximum(count)}')
