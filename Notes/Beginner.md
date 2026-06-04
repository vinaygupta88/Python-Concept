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

## Day 2
<h2>Strings</h2>
Strings are sequence of characters written inside quotes. It can include letters, numbers, symbols and spaces. A single character is treated as a string of length one.<br>
Strings can be created using either single ('...') or double ("...") quotes. Both behave the same.<br>
Use triple quotes ('''...''' ) or ( """...""") for strings that span multiple lines. Newlines are preserved.
<h4>Basic operations</h4>

```
1. Accessing Characters in String:
        Strings are indexed sequences. Positive indices start at 0 from the left, negative indices start at -1 from the right.
        example:-       
                        s = "ABCDEF"
                        print(s[0])   
                        print(s[4])

2. String Slicing:
        Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
        example:
                s = "ABCDEF"
                print(s[1:4])    
                print(s[:3])     
                print(s[3:])    
                print(s[::-1])

3. String Immutability:
        Strings are immutable, meaning their values cannot be changed after creation. Any modification to a string creates a new string instead of altering the original one.
        example:                s = "aBCDEF"
                                s = "A" + s[1:]  
                                print(s)

4. Deleting a String:
        Individual characters of a string cannot be deleted because strings are immutable. However, an entire string variable can be removed using del keyword
        exapmle:                s = "ABC"
                                del s

5.  Updating a String:
        Strings cannot be changed directly after creation. So any modification results in a new string being created using slicing or methods like replace().
        example:                s = "ABCD EF"
                                s1 = "H" + s[1:]                  
                                s2 = s.replace("ABC", "abc")  
                                print(s1)
                                print(s2)

```
<h4>Methods in Strings</h4>

```
1. **len():** returns the total number of characters in a string (including spaces and punctuation).
        eg:-    s = "GeeksforGeeks"
                print(len(s))
2. **upper() and lower():** upper() method converts all characters to uppercase whereas, lower() method converts all characters to lowercase.
        eg:-    s = "Hello World"
                print(s.upper())
                print(s.lower())
3. **strip() and replace():** strip() removes leading and trailing whitespace from the string and replace() replaces all occurrences of a specified substring with another.
        eg:-    s = "   ABC   "
                print(s.strip()) 
4. **Concatenation:** Strings can be combined by using + operator.
        eg:-    s1 = "Hello"
                s2 = "World"
                print(s1 + " " + s2)
5. **Repetition:** A string can be repeated multiple times using *. 
        eg:-    s = "Hello "
                print(s * 3)
<h4>Formatting Strings</h4>

- **f-strings:** f-strings allows to directly insert variables and expressions inside a string using {} brackets.
        eg:-    name = "Jake"
                age = 22
                print(f"Name: {name}, Age: {age}")
- **format():** format() method allows inserting values into placeholders {} inside a string.
        eg:-    s = "My name is {} and I am {} years old.".format( "Emily", 22)
```
<h4>Strings Functions</h4>

1. endswith("substring"): Return true if string end with substring.
2. capitalize(): Capitalizes 1st Character
3. replace(old,new): Replace all ocurrence of old string with new one
4. find(words): Return 1st index of 1st occure
5. count("substring"): Count the occurence of substring.

<h2>Conditional  Statements</h2>
Conditional statements are used to control the flow of execution in a program based on specific conditions. They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.

1. **if Statement:** If statement is used to execute a block of code only when a specified condition evaluates to True.<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260319073415383622/1.webp" height="200px">
2. **If Else:** statement is used to execute one block of code when the condition is True and another block when the condition is False.<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260319073523078423/2.webp" height="200px">
3. **If-elif-else Statement:** 
```
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```
4. **Nested if-else statement** is an if-else statement placed inside another if or else block. It is used to check conditions within another condition
```
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```
<b>Task 2 </b> a. Write a program to find the greatest of 3 numbers entered by the user.
                b. Write a program to check if a number entered by the user is odd or even.
                c. WAP to check if the munber is multiple of 7 or not