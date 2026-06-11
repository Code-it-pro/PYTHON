def tables(num):
    table = ""
    for i in range(1, 11):
        table += f"{num} X {i} = {num*i}\n"
    with open(f"Tables/table_{num}.txt", "a") as f:
        f.write(table)

for i in range(2, 21):
    tables(i)

print("Tables generated!")