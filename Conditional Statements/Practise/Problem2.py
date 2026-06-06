n1 = int(input("Enter marks of subject 1: "))
n2 = int(input("Enter marks of subject 2: "))
n3 = int(input("Enter marks of subject 3: "))

total_percentage = (n1 + n2 + n3) / 300 * 100

if(total_percentage >= 44 and n1 >= 33 and n2 >= 33 and n3 >= 33):
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam. Better luck next time: ", total_percentage)