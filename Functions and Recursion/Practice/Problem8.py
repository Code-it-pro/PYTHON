def tables(n):
    for i in range(1, 11):
        print(f'{n} X {i} = {n*i}')
    return

n = int(input("Enter a number for table: "))

tables(n)