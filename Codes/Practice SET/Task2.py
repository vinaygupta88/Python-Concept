# Write a program to input user's first name & print its length.
name = input("Enter your first name: ")
print("Your Name length: ", len(name))

# Write a program to find the occurrence of '$' in a String.
str = "Hi, $I am the $ symbol $99.99"
print("\n$ is occure: ", str.count("$"))

# Write a program to print the Grad of an student

marks = int(input("Enter your Marks: "))
if marks >= 90:
    print("A")
elif marks <= 80 and marks > 70:
    print("B")
elif marks <= 70 and marks > 60:
    print("C")
elif marks <= 60 and marks > 50:
    print("D")
else:
    print("F")


# WAP to check if the munber is multiple of 7 or not

num = int(input("Enter number : "))
if num % 7 == 0:
    print(num," is multiple of 7")
else:
    print(num," is not multiple of 7")