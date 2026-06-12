# Write a program to find the factorial of first n numbers(using for)

num = int(input("Enter the number : "))
factorial = 1

for fact in range(1, num+1):
    factorial *= fact
print(f'Factorial of {num} is {factorial}')