num = int(input("Enter a number to check Prime : "))
count = 0

for i in range(1,num+1):
    if(num%i==0):
        count +=1

if(count == 2 or num == 1 ):
    print(f'{num} is a Prime Number')
else:
    print(f'{num} is not Prime')