print("Hello Vinay, U write firest progam in Python series.\n")

# Variable
print("\n Variable\n")
name = "John"
age = 23
salary = 5000
print("Name: ", name)
print("Age: ", age)
print("Salary: ", salary)
print(type(age), "\n")

print("\nDATA TYPE\n")
# NUMERIC:
print("Numeric\n")
a = 5  # integer
b = 5.0  # Float
c = 2 + 4j  # Complex
sum = a + b
print(type(a))
print(type(b))
print("Sum: ", sum)
print(type(c), "\n")

# STRING:
print("\nString\n")
s = "Welcome to the Geeks World"
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1], "\n")

# LIST:
print("\nLIST:\n")
a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3], "\n")

# TUPLE:
print("\nTUPLE:\n")
t1 = (1,)
print(type(t1))

t2 = ("Geeks", "For", "Geeks", 1, 2)
print(t2[3])
print(t2[-3], "\n")

# BOOLEAN:
print("\nBOOLEAN:\n")
print(type(True))
print(type(False), "\n")

# SET:
print("\nSET:\n")
s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)
print("\n")

# DISCTIONARY:
print("\nDICTIONARY:\n")
d = {1: "Geeks", 2: "For", 3: "Geeks"}
print(d[1])
print(d.get(2))


print("\nOPERATORS\n")
# Arithmetic
a = 5
b = 2
print("Sum: ", a + b)
print("Diff: ", a - b)
print("Mul: ", a * b)
print("Div: ", a / b)
print("Flor div: ", a // b)
print("Modulo: ", a % b)
print("Power: ", a**b, "\n  ")

# Relational
print(10 == 10)  # True

# Logical
print(True and False)  # False

# Bitwise
print(5 | 3)  # 7

# Assignment
x = 10
x += 5
print(x)  # 15

# Ternary
age = 18
status = "Adult" if age >= 18 else "Minor"

# Identity
a = [1, 2]
b = a
print(a is b)  # True


print("\nCONVERSION\n")
# implicite
x = 10  # Integer
y = 10.6  # Float
z = x + y
print("x:", type(x))
print("y:", type(y))
print("z =", z)
print("z :", type(z))

# explicit
s = "100"  # String
a = int(s)
print(a)
print(type(a))

print("\nInput form USER\n")
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name)
print(age)
print("age type", type(age), "\n")
Age = int(input("Enter your age: "))
print(Age)
print("Age type", type(Age))
