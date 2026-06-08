def average(count):
    l1 = []
    for i in range(count):
        print(f"Enter {i+1} number ", end="")
        l1.append(int(input(": ")))
        # print("")

    n = len(l1)

    print(f'your numbers:\n{l1}')
    avr = sum(l1)/n
    print(f'Average of {n} numbers : {avr}')

count = int(input("Enter no. of numbers you need average for : "))

average(count)