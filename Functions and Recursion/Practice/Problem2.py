def CelToFahren(c):
    f = (c * (9/5)) + 32
    return f

c = int(input("Enter temperature in Celsius: "))

print(f'Fahrenheit: {CelToFahren(c)}')
