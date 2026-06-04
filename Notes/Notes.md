## Day 1
<h2>Introduction to Python</h2>
<p>Python is High level programing language, whre all the code is written in HLL(generaly in english).<br>

- Python is simple & easy.
- Free and open source
- Developed by **Guido van Rassum**
- Python is case Sensetive. (means A and a are totally differ).
- Portable and its use **Interpreter** to to change HLL into Machine level language.<br>
*example: print("Hello Vinay, Write first program")*
</p>
<h3>Variable</h3>
A Variable is name given to a memory location in a program.<br>Variables are used to store data that can be referenced and manipulated during program execution.<br>Python variables do not require explicit declaration of type. <a href="https://www.geeksforgeeks.org/python/python-variables/">Variable in python</a><br>
<p>Rules for Naming Variables</p>

- Names can contain (uppercase/ lowercase) letters, digits and underscores (_)
- The first character cannot be a digit
- Names are case-sensitive, so myVar and myvar are treated differently.
- Keywords such as if, else and for cannot be used as variable names.
- We can't use special symbols like !,@,#,$,% etc.
* type() function is used to print data type of variable.
<h3>Data Type</h3>
Data types are used to define the type of value stored in a variable. They determine what kind of operations can be performed on the data. In Python, everything is treated as an object and each value belongs to a specific data type.<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20241210131752166623/Python-Data-Types.webp" height="250px" alt="python Data Type"> <br>

- **Integers :** value is represented by int class. It contains positive or negative whole numbers 
- **Float :** value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point.
- **Complex :** It is represented by a complex class. It stores numbers with real and imaginary parts. For example: 2+3j
- **Strings :** are used to store text data. A string is represented using the str class and can be created using single, double or triple quotes.
- **Lists :** are ordered and mutable collections used to store multiple items in a single variable. Elements in a list can be of different data types and are accessed using indexing.
- **Tuples :** are ordered and immutable collections used to store multiple items in a single variable. Once created, tuple elements cannot be modified and are accessed using indexing.
- **Boolean: ** data type represents one of two values: True or False. It is mainly used in conditions and comparisons and is represented by the bool class.
- **Sets :** are unordered and mutable collections used to store unique elements. Since sets are unordered, elements cannot be accessed using indexing. Elements are usually accessed by iterating through the set using a loop.
- **Dictionaries :** are used to store data in key:value pairs. Each key in a dictionary must be unique and values are accessed using their keys with square brackets [] or get() method.
```
Example of DATA Type:

NUMERIC:
        a = 5               // integer
        b = 5.0            // Float
        c = 2 + 4j         // Complex

        print(type(a))
        print(type(b))
        print(type(c))

STRING:
        s = 'Welcome to the Geeks World'
        print(s)
        print(type(s))

        # access string with index
        print(s[1])
        print(s[-1])

LIST:
        a = [1, 2, 3]
        print(a)

        b = ["Geeks", "For", "Geeks", 4, 5]
        print(b[3])
        print(b[-3])

TUPLE:
        t1 = (1,)
        print(type(t1))

        t2 = ('Geeks', 'For', 'Geeks', 1, 2)
        print(t2[3])
        print(t2[-3])

BOOLEAN:
        print(type(True))
        print(type(False))

SET:
        s1 = {"a", "a", "b", "c", "b"}
        print(s1)

        s2 = {"Geeks", "For", "Geeks"}
        for i in s2:
            print(i)

DISCTIONARY:
        d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
        print(d[1])    
        print(d.get(2))
```
- **KeyWords :** These are the reserved words in python. like:- and,else,in,as,break,return, class, False, True, with, etc.<br>
Identifiers can't name of keywords.
- **Comment :** These are the line which is not part of code (interpreter can't run . ignore it).

<h3>Operators</h3>
Operators in general are used to perform operations on values and variables. <br>

**Operands :** Value on which the operator is applied.<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260501155121455689/pythiob-operators.webp" height="250px" alt="Operators">

<h3>Conversion</h3>
Type conversion in Python is the process of changing a value from one data type to another.

- Helps ensure correct operations and calculations.
- Examples include converting an integer to a float or a numeric string to an integer.
- Python supports two types of type conversion: Implicit Conversion and Explicit Conversion.

1. **Implicit Type Conversion :** Implicit conversion in Python happens automatically when different data types are used together in an expression.
        * Python converts a smaller data type to a larger one when needed.
        * Commonly occurs when integers and floats are combined.
        * Conversion happens at runtime to keep results accurate.
```
Example:
        x = 10          # Integer
        y = 10.6        # Float
        z = x + y     

        print("x:", type(x))
        print("y:", type(y))
        print("z =", z)
        print("z :", type(z))
```

2.  **Explicit Type Conversion :** Explicit conversion, also called type casting, is when a programmer manually changes a value from one data type to another.
        * Done using Python’s built-in functions like int(), float(), and str()
        * Gives full control over how data is interpreted or processed.
        * Used when automatic conversion is not suitable.
```
Example: 
        s = "100"  # String
        a = int(s)             
        print(a)
        print(type(a))
```
<h3>Input From USER</h3>

In python **input()** built inn function is used to take the input from the user using KEYBOARD.
- Result of input() is always a string. we have to type cast it to change in any other formate.
        eg:-    int(input()) for integers
                float(input())
<b>TASK 1 :</b>a. Write a program to input 2 numbers & print their sum, product, modulo, difference.
        b. Write a programm to input side of a sqaure and print its area