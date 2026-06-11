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

## Day 3
<h2>List and Tuple</h2>
<h3>List</h3>
List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.

- **Mutable**: list elements can be changed, updated, added, or removed after the list is created.
- **Ordered:** elements maintain the order in which they are inserted.
- **Index-based:** elements are accessed using their position, starting from index 0.
<h4>Creating List</h4>

- **Using Square Brackets:** Square brackets [] are used to create a list directly.<br>Example:-  a = [12,23, 34]
- **Using list() Constructor:** A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor.<br>Example:-  a = list((1, 2, 3, 'apple', 4.5))
- **Creating List with Repeated Elements:** A list with repeated elements can be created using the multiplication (*) operator.<br>Example:-  a = [2] * 5
- **Accessing List Elements :** Elements in a list are accessed using indexing. Python uses zero-based indexing, meaning a[0] represents the first element.
```
a = [10, 20, 30]
print(a[0])
print(a[-1])
```
<h4>Adding Elements into List</h4>

- **append():** Adds an element at the end of the list. Eg:- variable_name.append(Value)
- **insert():** Adds an element at a specific position. Eg:- variable_name.insert(position, value)
- **extend():** Adds multiple elements to the end of the list. Eg:- variable_name.extend(value/list)

<h4>Removing Elements from List</h4>

1. **remove():** Removes the first occurrence of an element.
2. **pop(index)**: Removes the element at a specific index or the last element if no index is specified.
3. **del statement:** Deletes an element at a specified index.
4. **clear():** removes all items.

```
a = [1, 2]

a.append(3)
a.insert(1, 2)
a.extend([3, 4])
a[1] = 25                       # udating list by index value
a.remove(2)
a.pop()
del a[1]
a.clear()
```

<h4>List methods</h4>

**Example:-** *lst = [2,1,3]*
1. lst.sort()   #sorts in ascending order       [1,2,3]
2. lst.sort(reverse=True)       # sorts in descending order     [3,2,1]
3. lst.reverse()                # reverse list  [3,2,1]

<h3>Tuple</h3>
A tuple is an immutable ordered collection of elements.

- Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
- Can hold elements of different data types.
- These are ordered, heterogeneous and immutable.
- A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items. Eg:- tup = ()           tup = ('Geeks', 'For')
- **For single value tuple must to add comma after value to treet as tuple other wise interpreter identify that as int, float, or string**
<h4>Tuple Basic Operations</h4>
Concatenation of Tuples : Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.

```
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)
```
Slicing of Tuple : Slicing a tuple means creating a new tuple from a subset of elements of the original tuple. The slicing syntax is tuple[start:stop:step].

```
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])
```
Deleting a  : Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.
```
tup = (0, 1, 2, 3, 4)
del tup
print(tup)
```
Tuple Unpacking with Asterisk (*): *operator is used in tuple unpacking to grab multiple items into a list. This is useful to extract just a few specific elements and collect the rest together.
```
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)
```
Converting a List to a Tuple: We can convert a list in Python to a tuple by using the tuple() constructor and passing the list as its parameters.
```
# Code for converting a list and a string into a tuple
a = [0, 1, 2]
tup = tuple(a)

print(tup)
```

Tuple Packing
```
# Tuple packing
a, b, c = 11, 12, 13
tup = (a, b, c)
print(tup)
```
<h4>Tuple Built-In Methods</h4>
Tuples support only a few methods due to their immutable nature. The two most commonly used methods are count() and index()

1. **index( ) :** Find in the tuple and returns the index of the given value where it's available.
2. **count( ):** Returns the frequency of occurrence of a specified value.
<table style="text-align:center;border:1px solid black;border-collapse:collapse;">
    <tr>
        <th style="border:1px solid black;padding:8px;">Parameter</th>
        <th style="border:1px solid black;padding:8px;">List</th>
        <th style="border:1px solid black;padding:8px;">Tuple</th>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Mutability</td>
        <td style="border:1px solid black;padding:8px;">Lists are mutable (can be modified).</td>
        <td style="border:1px solid black;padding:8px;">Tuples are immutable (cannot be modified).</td>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Iteration Speed</td>
        <td style="border:1px solid black;padding:8px;">Iteration over lists is time-consuming.</td>
        <td style="border:1px solid black;padding:8px;">Iteration over tuples is faster.</td>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Operations</td>
        <td style="border:1px solid black;padding:8px;">Lists are better for insertion and deletion operations.</td>
        <td style="border:1px solid black;padding:8px;">Tuples are more suitable for accessing elements efficiently.</td>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Memory Usage</td>
        <td style="border:1px solid black;padding:8px;">Lists consume more memory.</td>
        <td style="border:1px solid black;padding:8px;">Tuples consume less memory.</td>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Built-in Methods</td>
        <td style="border:1px solid black;padding:8px;">Lists have several built-in methods.</td>
        <td style="border:1px solid black;padding:8px;">Tuples have fewer built-in methods.</td>
    </tr>
    <tr>
        <td style="border:1px solid black;padding:8px;">Error Prone</td>
        <td style="border:1px solid black;padding:8px;">Lists are more prone to unexpected changes and errors.</td>
        <td style="border:1px solid black;padding:8px;">Tuples, being immutable, are less error-prone.</td>
    </tr>
</table>

<b>Task 3 :</b> a. Write to ask the user to enter names of theri 3 favorite movies & store them in a list.
                b. Write to check if a list contains a palindrome of element.(Hint: used copy() method)
                c. Write a program to count the number of students with the "A" grade in the following tuple. Store the above values in a list & sort then from "A to D".

## Day 4
<h2>Dictonary & Sets</h2>
Dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), values can be of any data type, whether mutable or immutable. It could not allow duplicated keys.

- A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:). A dictionary can also be created using dict() function.
- **Accessing Dictionary Items :** A value in a dictionary is accessed by using its key. This can be done either with square brackets [ ] or with the get() method. Both return the value linked to the given key.
- **Adding and Updating :** New items are added to a dictionary using the assignment operator (=) by giving a new key a value. If an existing key is used with the assignment operator, its value is updated with the new one.
<h5>Removing Dictionary Items</h5>

1. **del:** removes an item using its key.
2. **pop():** removes the item with the given key and returns its value
3. **popitem():** removes and returns the last inserted key-value pair
4. **clear()**: removes all items from the dictionary

```
# Accessing dictionary Items
d = {"name": "Sam"}
d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

# Del methods

d = {"a": 1, "b": 2}
del d["a"]
print(d)

# pop method

d = {"a": 1, "b": 2}
val = d.pop("a")
print(val)
print(d)

#pop items
d = {"a": 1, "b": 2}
print(d.popitem())

#clear methods
d = {"a": 1, "b": 2}
d.clear()
print(d)


```
<h4>Dictionary Methods</h4>
Example: myDict = {"a": 1, "b": 2,"c":3,"d":4}

1. myDict.keys()                # returns all keys
2. myDict.values()              # return all values
3. myDict.items()               # return all (key, value) pairs as tuple
4. myDict.get("key")            # return the key according to values
5. myDict.update(newdict)       # insert the specified item to the dictionary
6. **Iterate key-value pairs :**  Returns all key-value pairs as tuples.
```
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)
```
<h4>Nested Dictionaries</h4>
A nested dictionary is a dictionary that contains another dictionary as one of its values. Below diagram shows how a nested dictionary works, where key 3 points to another dictionary inside the main dictionary.<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260110161344925940/keys.webp" height=200px>

```
d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])
```
<h2>SET<h2>
Set is used to store a collection of unordered items.

- No duplicate elements. If you try to insert the same item again, it is ignored because sets store only unique values.
- An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
- **set() method** is used to convert other data types, such as lists or tuples, into sets.
- Sets can store heterogeneous elements in it, i.e., a set can store a mixture of string, integer, boolean, etc datatypes.
<h4>Set Methods</h4>
Python set methods are built-in functions used to add, remove, update and perform other operations on sets. These methods help manage and manipulate set elements efficiently.

Example: st = {1,2,3,4,5,6,7,8,9}

1. **st.add(el)**: Adds an element to the set.
2. **st.clear():** Removes all elements from the set.
3. **st.copy():** Returns a shallow copy of the set.
4. **st.difference():** Returns a set containing elements present in the first set but not in the second set.
5. **st.difference_update():** Removes common elements from the original set.
6. **st.discard():** Removes an element from the set if it exists.
7. **st.pop():** Removes and returns a random element from the set.
7. **st.remove(el):** Removes the specified element from the set.
8. **frozenset():** Creates an immutable set.
<h4>SET Operation</h4>

1. Union of Sets: union() function combines two sets and returns a new set with all unique elements.
2. Intersection of Sets: intersection() function returns a new set containing elements that are common to both sets.
3. Difference of Sets: difference() function returns a set containing elements that are in the first set but not in the second.
4. Symmetric Difference of sets : The symmetric difference of two sets includes elements that are in either set but not in both.
```
s = {10, 50, 20}
print(s)
print(type(s))

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# adding
s = {"a", "b", "c"}
s.add("d")
print(s)

#Union
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# Intersection
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

#Set differenc
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

# cleaning Set
s = {1, 2, 3}
s.clear()
print(s)


# copy method
s = {1, 2, 3}
c = s.copy()
print(c)        

# Frozen set
s = frozenset([1, 2, 3])
print(s)

# Symmetry Difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '^' operator
res1 = A ^ B
print("using '^':", res1)

# Using symmetric_difference() method
res2 = A.symmetric_difference(B)
print("using symmetric_difference():", res2)

```

<b>Task 4: </b> a. Store following word meanings in python dictionary:<br>
        table:"a piece of furniture","list of facts & Figures"<br>
        cat:"a small animal" <br>
        
        b. you are given a list of subjects for students, Assume one classroom is requireed for 1 subject. How many classrooma are needed by all students. <br>
        "python","Java","C++","python","javascript","java","python","java","C++","C"