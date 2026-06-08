# formula: cm = inches × 2.54

def incheToCm(inches):
    return inches * 2.54

n = int(input("Enter length in inches: "))
print(f'Inches to Centimeters = ',end="")
print(incheToCm(n),"cm")