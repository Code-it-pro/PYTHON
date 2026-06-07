num = int(input("Enter a number : "))

sum = 0

# for i in range(1, num+1):
#     sum +=i
#     print(i)

# print(f'Sum of all natural numbers till {num} = {sum}')

i = 1

while(i < num+1):
    sum +=i
    print(i)
    i +=1

print(f'Sum of all natural numbers till {num} = {sum}')