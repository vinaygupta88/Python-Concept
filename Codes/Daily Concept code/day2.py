# Accessing Characters in String
s = "ABCDEF"
print(s[0])   
print(s[4])

#String Slicing
s = "ABCDEF"
print(s[:3])     
print(s[1:4])    
print(s[3:])    
print(s[::-1])

# String lenth
s = "GeeksforGeeks"
print(len(s))

#Upper lower
s = "Hello World"
print(s.upper())
print(s.lower())

#Concatation
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#Formatting

name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")

# endwith function

str = "I am Coder"
print(str.endswith("er"))