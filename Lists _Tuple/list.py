number = [12, 232, 3, 45,12350, 5123,5123, 12350, 2356, 714, 538, 9, 12350]
print(type(number))

number[4] = 5125345
print(number)

number.append("Hello")
number.append("Pop-me")
number.append("dont touch me")
print(number)

number.insert(14,1000000)
print(number)

number.count(12350)
print(number)

number.index("Pop-me")
print(number)

number.remove("dont touch me")
print(number)

value = number.pop(3)
value2 = number.pop(-1)
value3 = number.pop(-2)
value4 = number.pop(-3)
print(value)
print(value2)
print(value3)
print(value4)

number.sort()
print(number)

print(number[0:10:2])

number.reverse()
print(number)