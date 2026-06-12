with open("log.txt") as file:
    lines = file.readlines()
    # print(lines)
    lineno = 1
    for line in lines:
        # print(line)
        if "Python" in line:
            print(f"Yes, python is present, lineno: {lineno}")
            break
        lineno += 1