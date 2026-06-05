# Write a program to find the greatest of 3 numbers entered by the user.

num1 = float(input("Enter the First Number : "))
num2 = float(input("Enter the Second Number : "))
num3 = float(input("Enter the Third Number : "))

if (num1 > num2 and num1 > num3):
    print(num1," is grestest")
elif(num2 > num1 and num2 > num3):
    print(num2, " is greatest")
else:
    print(num3, " is greatest")