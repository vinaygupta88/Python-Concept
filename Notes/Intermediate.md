## Day 7
<h2>List Comprehension</h2>
List comprehension is a concise way to create new lists by applying an expression to each item in an existing iterable like a list, tuple or range. It helps to write clean, readable and efficient code compared to traditional loops.<br><br>

*syntax :* [expresion  for iterator in iterable if condition] <br>
*Paramenter :*
- **expression:** operation or value to include in the new list.
- **iterator:** current element from the iterable.
- **iterable:** sequence like a list, tuple or range.
- **if condition (optional):** filter to include only items that satisfy the condition.

```
# square of each element
a = [2, 3, 4, 5]
res = [i ** 2 for i in a]
print(res)
```
<h4>Using if-else</h4>
This method applies an if-else condition directly inside the list comprehension. Each element is checked and a corresponding value is added to the new list.

```
a = [1, 2, 3, 4, 5]
res = ['Even' if n % 2 == 0 else 'Odd' for n in a]
print(res)
```
---
<h2>Lambda Functions</h2>
Lambda functions are small anonymous functions, meaning they do not have a defined name. These are small, short-lived functions used to pass simple logic to another function.<br>

*syntax :* function_name = lambda argument :expression

- Contain only one expression.
- Result of that expression is returned automatically (no return keyword needed).
```
a = 'sangaButtapandu'
upper = lambda x: x.upper()  
print(upper(a))
```
- **Returning Multiple Results:** Although a lambda can contain only one expression, it can still return multiple results by combining them into a tuple.
```calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
```
<h4>method use by lambda</h4>

1.  **filter():** This function uses a lambda expression to select elements from a list that satisfy a given condition, such as keeping only even numbers.
2.  **map():** This function applies a lambda expression to each element and returns a map object. It can be converted to a list using list().
3. **reduce():** This function repeatedly applies a lambda expression to elements of a list to combine them into a single result.
```
#Filter

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

# map
a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))

# reduce

from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)
```

<h2>Iterators & Generators</h2>
<h3>Iterator</h3>
An iterator is an object that lets you access items in a sequence one at a time. It does not load the entire data at once, instead it gives one value when asked. This saves memory and follows lazy evaluation (creates values only when needed).

```
l = iter(['Geeks', 'For', 'Geeks'])
print(next(l))
print(next(l))
print(next(l))

Explanation:
    * iter() converts the list into an iterator.
    * next() fetches values one by one.
    * It remembers its position and does not restart automatically.
```
<h3>Generators</h3>
A generator is another way to create iterators, but in a simpler and more readable manner. Instead of storing all values, generators produce values on the fly using the <b>yield</b> keyword.

```
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a = sq_numbers(3)

print("The square of numbers 1, 2, 3 are:")
print(next(a))
print(next(a))
print(next(a))

Explanation:
    * yield sends one value at a time without ending the function.
    * Each next() call resumes the function from where it stopped.
    * Values are produced only when needed.
```
---
## Day 8
<h2>File Handling (File I/O)</h2>
File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.

- Store data permanently, even after the program ends.
- Access external files like .txt, .csv, .json, etc.
- Process large files efficiently without using much memory.
- Automate tasks like reading configs or saving outputs.<br>
<b>Type of File :</b><br>
    a. Text Files: .txt, .docx, .log, .csv etc.<br>
    b. Binary Files: .mp4, .mov, .png, .jpeg etc.<br>
<b>Mode in File Handling</b><br>
    a. **Read** ('r'): Read-only. Raises I/O error if file doesn't exist. <br>
    b. **Write** ('w'): Write-only. Overwrites file if it exists, else creates a new one. <br>
    c. **Append** ('a'): Append-only. Adds data to end. Creates file if it doesn't exist. <br>
    d. **Binary** ('b'): Used for non-text files like images or audio. Always combined with 'r', 'w', or 'a. <br>
    e. **Read and Write** ('r+'): Read and write. Raises I/O error if the file does not exist. <br>
    f. **Write and Read** ('w+'): Read and write. Overwrites file or creates new one.
    g. **Read** ('r'): Read-only. Raises I/O error if file doesn't exist. <br>
<h4>Operation in File Handling</h4>

1. **open() :** This operation is done before reading and writing the file. This required file path and mode as arguments.<br>
    *Syntax :* file_object = open("file_name","mode") <br>
    * if file is in same location then only name is required else complete file path is required.
    * mode in which you want to open the file (read, write, append, etc.)
2. **close() :** close() method closes the file and releases the system resources. If the file was opened in write or append mode, closing ensures that all changes are properly saved.<br>
    *syntax :* file_object.close()
3. **Reading file :** Used to read the file, there are three methods:-<br>
    a. read(): The read() method returns the whole text, but you can also specify how many characters you want to return. <br>
    b. readline() : It return one line. <br>
    c. readlines(): It return the list of all line.<br>
4. **Writing file :** This creates a new file if it doesn’t exist, or overwrites the existing file if it does. The write() method is used to add content. After writing, make sure to close the file. <br>
    a. write() : used to write singl string in file <br>
    b. writelines() : Writes multiple strings from a list to a file.
5. **Using with Statement**: Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing. This reduces the risk of file corruption and resource leakage.<br>
```
with open("geek.txt", "r") as file:
    content = file.read()
    print(content)
```
- <b>tell() : </b> Returns current cursor position.
- <b>seek() : </b> Moves cursor position.
```
with open("data.txt", "r") as file:
    print(file.tell())
```
```
# 1. OPEN FILE IN READ MODE
file = open("sample.txt", "r")
print(file.read())
file.close()

# 2. OPEN FILE IN WRITE MODE (OVERWRITES CONTENT)
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()

# 3. OPEN FILE IN APPEND MODE
file = open("sample.txt", "a")
file.write("\nNew Line Added")
file.close()

# 4. CREATE NEW FILE USING x MODE
file = open("newfile.txt", "x")
file.close()

# 5. READ ENTIRE FILE
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 6. READ FIRST 10 CHARACTERS
with open("sample.txt", "r") as file:
    print(file.read(10))

# 7. READ ONE LINE
with open("sample.txt", "r") as file:
    print(file.readline())

# 8. READ ALL LINES AS LIST
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# 9. WRITE MULTIPLE LINES
with open("sample.txt", "w") as file:
    file.writelines([
        "Apple\n",
        "Banana\n",
        "Mango\n"
    ])


# 10. FILE PROPERTIES
with open("sample.txt", "r") as file:
    print("Name :", file.name)
    print("Mode :", file.mode)
    print("Closed :", file.closed)

# 11. EXCEPTION HANDLING
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File Not Found")


# 12. DELETE FILE
import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File Deleted")
else:
    print("File Not Found")

# 13. RENAME FILE
import os

os.rename("old.txt", "new.txt")


# 14. WRITE BINARY FILE
with open("binary.bin", "wb") as file:
    file.write(b"Hello World")

# 15. READ BINARY FILE
with open("binary.bin", "rb") as file:
    data = file.read()
    print(data)


# 16. CSV FILE WRITING
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Rahul"])
    writer.writerow([2, "Aman"])

# 21. JSON FILE WRITING
import json

student = {
    "id": 1,
    "name": "Rahul",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```
<b>Task 8: </b><br>
    a. Create a new file "practice.txt" using python . Add the following data inn it-<br>
        ```
        Hi everyone 
        we are learning File I/O
        using Python
        I like programming in Python
        ``` 
    <br>        
    b. Write a function that replace all occurance of "python" with "java" in above file.<br>
    c. Search if the word "learninng" exists in the file or not.

---
## Day 9
<h2>Object Oriented Programming (OOPS)</h2>
Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260605123244175152/object_oriented_programming.webp" height=250px><br>

<h5>Class</h5>
A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.
    
- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute
```
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
```
<h5>Objects</h5>
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

- State: represented by the attributes and reflects the properties of an object.
- Behavior: represented by the methods of an object and reflects the response of an object to other objects.
- Identity: gives a unique name to an object and enables one object to interact with other objects.

```
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)
```
<p>Any objects is delete by using 'del' keywords Ex:- del person <br>
<h5> __init__() </h5>
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.<br>
The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

- init function use alway "self" argument as reference <br>
The self parameter is a reference to the current instance of the class.<br>
It is used to access properties and methods that belong to the class.
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print(f'{sel.name} good morning')

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
p1.greet()
```
<br>
<table>
    <thead>
        <tr>
            <th>Aspect</th>
            <th>Class Attributes</th>
            <th>Instance Attributes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Definition</td>
            <td>Defined within the class block but outside of methods</td>
            <td>Defined within methods, typically the <code>__init__</code> constructor</td>
        </tr>
        <tr>
            <td>Scope</td>
            <td>Shared among all instances of the class</td>
            <td>Specific to each instance of the class</td>
        </tr>
        <tr>
            <td>Access</td>
            <td>Accessed using the class name or any instance</td>
            <td>Accessed using an instance of the class</td>
        </tr>
        <tr>
            <td>Modification</td>
            <td>Changing affects all instances of the class</td>
            <td>Changing affects only the specific instance</td>
        </tr>
        <tr>
            <td>Storage Location</td>
            <td>Stored in the class namespace</td>
            <td>Stored in the instance namespace</td>
        </tr>
        <tr>
            <td>Usage</td>
            <td>Define properties common to all instances</td>
            <td>Define properties specific to each instance</td>
        </tr>
        <tr>
            <td>Example</td>
            <td><code>MyClass.class_attribute</code></td>
            <td><code>instance_name.instance_attribute</code></td>
        </tr>
    </tbody>
</table>

<b>Task 9 :</b><br>
    Create a class called Rectangle, Add an __init__ method with width and height, and store them as properties, Add a method called area that returns the width multiplied by the height, Create an object r1 with width 5 and height 3, Print the area of r1. <br>

---

## Day 10
<h2>Methods</h2>
Methods are functions that belong to a class. They define the behavior of objects created from the class.<br>

```
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


## Methods with Parameters
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
```
<h6>Static Methods</h6>
A static method in Python is a method defined inside a class that does not depend on any instance or class data. It is used when a function logically belongs to a class but does not need access to self or cls. Static methods help organize related utility functions inside a class without creating objects.<br>

```
syntax:
    class ClassName:
       @staticmethod                    #decoder
       def method_name(parameters):    
            method_body

Example: 
class Calc:
    @staticmethod           # @staticmethod: Declares the method as static
    def add(a, b):
        return a + b

res = Calc.add(2, 3)        # Normal function arguments (no self or cls)
print(res)
```
<b>Task 10 :</b><br>
Using staticmethod design a simple calculator

<h5>Basic Terminology</h5>

- **'del'** Used to delete object properties or object itself.<br>
    Eg:- [ del s1.name ] or [ del s1]
- **Private attribute :** These are ment to be used only within the class and are not accessible from outside the class. <br>
making the attribute private, we can use (__) double underscore.

```
# Private Attribute 
class Student:
    name = "Lokesh Singh" 
    __id = 1234  
    
    # Method for Printing Private Attribute
    def Print_Id(self):
        print(f"The Id of student is : {self.__id}")
    
lokesh = Student()
print(f"The name of student is : {lokesh.name}")  # Public Attribute can be accessed directly from outside class

lokesh.Print_Id()
```

- **Private Methods :**  Private methods are those methods that should neither be accessed outside the class nor by any base class.

```
# Creating a class
class A:

    # Declaring public method
    def fun(self):
        print("Public method")

    # Declaring private method
    def __fun(self):
        print("Private method")


# Driver's code
obj = A()

# Calling the private member
# through name mangling
obj._A__fun()
```
---
## Day 11
<h2>Four Pillars of OOPs</h2>
<h3>Inheritance</h3>
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). <br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260522161333480012/animal_class.webp" height=250px alt="Inheritance"> <br>

```
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()


Explanation: 
    * class Animal defines the parent class.
    * info() prints the name of the animal.
    * class Dog(Animal) defines Dog as a child of Animal class.
    * d.info() calls parent method info() and d.sound() calls child method
```
<h5>Benefits Of Inheritance</h5>

- Promotes code reusability by sharing attributes and methods across classes.
- Models real-world hierarchies like Animal -> Dog or Person -> Employee.
- Simplifies maintenance through centralized updates in parent classes.
- Enables method overriding for customized subclass behavior.
- Supports scalable, extensible design using polymorphism.

<h4>super() Function</h4>
super() function is used to call methods from a superclass following Python’s Method Resolution Order (MRO). In particular, it is commonly used in the child class's __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.

```
# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method

Explanation:
    * super() function is used inside __init__() method of Dog to call the constructor of Animal and initialize inherited attribute (name).

    * This ensures that parent class functionality is reused without needing to rewrite the code in the child class.
```
<h5>Method Overriding in Inheritance</h5>
Method overriding allows a child class to provide its own implementation of a method that already exists in the parent class. This enables customized behavior while still maintaining the inheritance relationship.

```
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()


Explanation:

   * Animal defines a method sound().
   * Dog inherits from Animal and overrides the sound() method.
   * When d.sound() is called, Python executes the overridden method in the child class instead of the parent class method.
```
<h4>Types of Inheritance in Python</h4>
Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance in Python<br><img src="https://media.geeksforgeeks.org/wp-content/uploads/20220707180832/typesofinheritance.gif" height=300px alt="Type of inheritance"><br>

<h5>Single Inheritance : </h5>
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

```
                    B ------> A
                
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver code
obj = Child()
obj.func1()
obj.func2()
```
<h5>Multiple Inheritance :</h5>
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.<br> <img src="https://media.geeksforgeeks.org/wp-content/uploads/20251009172626954371/MultipleInheritance.webp" height=200px alt="multiple inheritance">

```

# Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
```
<h5>Multilevel Inheritance :</h5>
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.<br>

```
# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
```
<h5>Hierarchical Inheritance :</h5>
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes. <br><img src="https://media.geeksforgeeks.org/wp-content/uploads/20251009172317410936/HierarchicalInheritance.webp" height=150px alt="Hierarchical Inheritance">

```
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()
```
<h5>Hybrid Inheritance :</h5>
Hybrid inheritance is a combination of more than one type of inheritance. It uses a mix like single, multiple, or multilevel inheritance within the same program. Python's method resolution order (MRO) handles such cases.<br>

```
# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()
```
<h4>Method Resolution Order in Python Inheritance [MRO]</h4>
Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes. It becomes important when the same method exists in more than one class in an inheritance chain, especially in multiple inheritance.

he example shows how Python decides which method to execute when both a parent and a child class have a method with the same name.

```
class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

a = B()
a.fun()

Explanation:
       * When obj.fun() is called, Python first looks in class B.
       * Since B defines fun(), it runs that method and does not check class A.
       * The MRO here is: B -> A.

----
Multiple Inheritance (Diamond Problem)

class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

class C(A):
    def fun(self):
        print("In class C")

class D(B, C):
    pass

a = D()
a.fun()


```
---
## Day 12
<h3>Polymorphism</h3>
Polymorphism means "many forms" and allows the same method, function or operator to behave differently depending on the object or data it works with. 

<h4>Types of Polymorphism</h4>
Polymorphism refers to the ability of the same method or operation to behave differently based on object or context. It mainly includes compile-time and runtime polymorphism. <br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20250924155521774996/polymorphism_in_java.webp" height=250px alt="Type of polymorphism"><br>


<h4>Compile-time Polymorphism</h4>
Compile-time polymorphism involves selecting a method or operation before program execution, typically through method or operator overloading.

```
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

```
<h4>Runtime Polymorphism (Overriding)</h4>
Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it. This happens through Method Overriding a child class provides its own version of a method already defined in the parent class.

```
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

```
<h4>Polymorphism in Built-in Functions</h4>
Python's built-in functions such as len() and max() are polymorphic because they work with different data types and return results based on type of object passed. This showcases it's dynamic nature, where same function name adapts its behavior depending on input.

```
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings

```

<h4>Polymorphism in Functions</h4>
Polymorphism allows functions to work with different object types as long as they support the required behavior. Using duck typing, it focuses on whether an object has the required methods rather than its type, enabling flexible and reusable code.

```
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())
```

<h4>Polymorphism in Operators</h4>
Same operator (+) can perform different tasks depending on operand types. This is known as operator overloading. This flexibility is a key aspect of polymorphism.

```
print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation
```
<h4>Method Overriding</h4>
Method overriding occurs when a child class defines a method with the same name as a method in its parent class. This allows the child class to provide its own implementation while retaining the inheritance relationship. It is commonly used to customize or extend the behavior of inherited methods.

```
class Animal:
    def display(self):
        print("This is an animal")

class Dog(Animal):
    def display(self):
        print("This is a dog")

obj = Dog()
obj.display()
```
---
## Day 13
<h3>Encapsulation</h3>
It refers to bundling data (attributes) and methods (functions) that operate on that data into a single unit (class) and restricting direct access to some of an object's internal details.<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260522161654499472/encapsulation_in_python.webp" height=250px alt="encapsulation"><br>

```
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
print(emp.__salary)
```

- Protects data from unauthorized access and accidental modification.
- Controls data updates using getter/setter methods with validation.
- Enhances modularity by hiding internal implementation details.
- Simplifies maintenance through centralized data handling logic.
- Reflects real-world scenarios like restricting direct access to a bank account balance.

<h5>Access Specifiers</h5>
Access specifiers define how class members (variables and methods) can be accessed from outside the class. They help in implementing encapsulation by controlling the visibility of data. There are three types of access specifiers:<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20250710130248628645/types_of_access_modifier.webp" height=200px alt="access specifiers"><br>

1. **Public Members :** Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).

```
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible
```
2. **Protected members :** Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).

```
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass
```
3. **Private members :** Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data. In Python, private members are defined with a double underscore prefix (e.g., self.__salary).

```
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly
```

<h3>Abstraction</h3>
Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user. It is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.<br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260520171243990924/data_abstraction.webp" height=250px><br>

- **Abstract Base Class (ABC)** is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.<br>

Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

```
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
```
- **Abstract methods** are method declarations without a body defined inside an abstract class. They act as placeholders that force subclasses to provide their own specific implementation, ensuring consistent structure across derived classes.
- **Concrete methods** are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality.
- **Abstract properties** work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties.
- 
<b>Task Abstraction:</b>
Create Account class with 2 attribute - balance and acoount_no. Create methods for debit,credit & printing the balance.