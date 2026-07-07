## Python Interview Questions and Answers

<h2>Basic Level</h2>

<h3>1. What is Python, and why is it widely used?</h3>
<p>Python is a high-level, interpreted programming language known for its simple syntax and readability. It is widely used in web development, data science, automation, AI, networking, and scripting because it is easy to learn and has a large ecosystem of libraries.</p>

<h3>2. What are variables in Python? What are the naming rules?</h3>
<p>Variables are used to store data values in memory. In Python, a variable name can contain letters, numbers, and underscores, but it cannot start with a number. Variable names are case-sensitive, and keywords like if, else, for, class cannot be used as variable names.</p>

<pre><code>name = "dev-vinay"
age = 22
_marks = 98
</code></pre>

<h3>3. What is the difference between a variable and a constant?</h3>
<p>A variable can be changed during program execution, while a constant is intended to remain fixed. Python does not have built-in constant types, but constants are usually written in uppercase to indicate they should not be changed.</p>

<pre><code>PI = 3.14
</code></pre>

<h3>4. What are Python data types? Name the common built-in data types.</h3>
<p>Python has several built-in data types such as int, float, complex, str, list, tuple, set, dict, and bool. These types define what kind of value a variable can hold and what operations can be performed on it.</p>

<h3>5. What is the difference between implicit and explicit type conversion?</h3>
<p>Implicit conversion is automatic and happens when Python converts smaller data types to larger ones during an operation. Explicit conversion is done manually using functions like int(), float(), and str().</p>

<pre><code>x = 10
 y = 2.5
 z = x + y

 s = "100"
 a = int(s)
</code></pre>

<h3>6. How does the input() function work in Python? Why is type casting needed?</h3>
<p>The input() function reads data entered by the user from the keyboard. It always returns a string, so if we want numeric input, we need to convert it using int(), float(), etc.</p>

<pre><code>name = input("Enter your name: ")
age = int(input("Enter your age: "))
</code></pre>

<h3>7. What is a string in Python? Why are strings immutable?</h3>
<p>A string is a sequence of characters enclosed in single or double quotes. Strings are immutable, which means once created, their contents cannot be changed. Any modification creates a new string.</p>

<pre><code>s = "hello"
print(s.upper())
</code></pre>

<h3>8. What is the difference between a list and a tuple?</h3>
<p>A list is mutable, meaning its elements can be changed, added, or removed. A tuple is immutable, so it cannot be modified after creation. Lists are commonly used when data changes, while tuples are used for fixed values.</p>

<pre><code>lst = [1, 2, 3]
tup = (1, 2, 3)
</code></pre>

<h3>9. What is a dictionary in Python? How is it different from a set?</h3>
<p>A dictionary stores data in key-value pairs and is unordered but indexed by key. A set stores only unique values and does not use key-value pairs.</p>

<pre><code>student = {"name": "Amit", "age": 20}
colors = {"red", "green", "blue"}
</code></pre>

<h3>10. What are conditional statements in Python?</h3>
<p>Conditional statements are used to execute code based on a condition. Python uses if, elif, and else to control the flow of execution.</p>

<pre><code>age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
</code></pre>

<h2>Intermediate Level</h2>

<h3>11. What is the difference between a while loop and a for loop?</h3>
<p>A while loop runs as long as a condition is true. A for loop is used to iterate over a sequence such as a list, tuple, string, or range.</p>

<pre><code>i = 0
while i < 5:
    print(i)
    i += 1

for i in range(5):
    print(i)
</code></pre>

<h3>12. What is the use of break, continue, and pass in loops?</h3>
<p>break stops the loop completely, continue skips the rest of the current iteration and moves to the next one, and pass is a placeholder that does nothing.</p>

<pre><code>for i in range(5):
    if i == 3:
        continue
    print(i)
</code></pre>

<h3>13. What is the range() function?</h3>
<p>The range() function generates a sequence of numbers. It is commonly used in for loops to repeat a task a specific number of times.</p>

<pre><code>for i in range(1, 10, 2):
    print(i)
</code></pre>

<h3>14. What is string slicing?</h3>
<p>String slicing is used to access a part of a string. It uses the syntax string[start:end]. The end index is excluded.</p>

<pre><code>s = "Python"
print(s[1:4])
print(s[::-1])
</code></pre>

<h3>15. What are some common string methods?</h3>
<p>Common string methods include upper(), lower(), strip(), replace(), split(), find(), and count(). These methods help manipulate and process strings efficiently.</p>

<pre><code>s = " Hello World "
print(s.strip())
print(s.upper())
</code></pre>

<h3>16. What is the difference between append(), insert(), and extend() in a list?</h3>
<p>append() adds a single element to the end, insert() adds an element at a specific index, and extend() adds multiple elements from another iterable.</p>

<pre><code>lst = [1, 2]
lst.append(3)
lst.insert(1, 10)
lst.extend([4, 5])
</code></pre>

<h3>17. How do you remove elements from a list?</h3>
<p>We can remove items using remove(), pop(), del, or clear(). remove() removes the first matching value, pop() removes by index, del removes by index or slice, and clear() removes all elements.</p>

<pre><code>lst = [10, 20, 30]
lst.remove(20)
print(lst)
</code></pre>

<h3>18. What is dictionary comprehension?</h3>
<p>Dictionary comprehension is a compact way to create dictionaries using a single line of code.</p>

<pre><code>numbers = {x: x * x for x in range(1, 6)}
print(numbers)
</code></pre>

<h3>19. What is a set, and how is it different from a list?</h3>
<p>A set is an unordered collection of unique elements. Unlike a list, it does not allow duplicate values and does not support indexing.</p>

<pre><code>s = {1, 2, 2, 3}
print(s)
</code></pre>

<h3>20. What is a function in Python? Why are functions useful?</h3>
<p>A function is a reusable block of code that performs a specific task. Functions reduce repetition, make code organized, and improve readability.</p>

<pre><code>def add(a, b):
    return a + b

print(add(2, 3))
</code></pre>

<h2>Intermediate to Advanced</h2>

<h3>21. What is recursion? What is a base case in recursion?</h3>
<p>Recursion is when a function calls itself. The base case is the condition that stops the recursion; otherwise, the function can run forever.</p>

<pre><code>def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
</code></pre>

<h3>22. What is the difference between a recursive function and an iterative function?</h3>
<p>A recursive function solves a problem by calling itself, while an iterative function uses loops to repeat steps. Recursion can be elegant for problems like tree traversal, but iteration may be more efficient and easier to debug.</p>

<h3>23. What are function arguments in Python?</h3>
<p>Function arguments are values passed into a function. Python supports positional arguments, keyword arguments, and default arguments.</p>

<pre><code>def greet(name, message="Hello"):
    print(message, name)

greet("Amit")
greet("Amit", "Hi")
</code></pre>

<h3>24. What is the difference between return and print in a function?</h3>
<p>print displays output on the screen, but return sends the value back to the caller. A function can print something, but if it has no return value, it returns None by default.</p>

<pre><code>def add(a, b):
    return a + b

result = add(3, 4)
print(result)
</code></pre>

<h3>25. What is the difference between list, tuple, set, and dictionary?</h3>
<p>List is ordered and mutable, tuple is ordered and immutable, set is unordered and contains unique elements, and dictionary stores data in key-value pairs. Each is used for different types of tasks.</p>

<h3>26. What is a nested dictionary?</h3>
<p>A nested dictionary is a dictionary that contains another dictionary as a value.</p>

<pre><code>student = {
    "name": "Sam",
    "details": {
        "age": 21,
        "course": "Python"
    }
}

print(student["details"]["course"])
</code></pre>

<h3>27. What is a lambda function?</h3>
<p>A lambda function is an anonymous function defined in one line using the lambda keyword. It is often used for short operations.</p>

<pre><code>square = lambda x: x * x
print(square(5))
</code></pre>

<h3>28. What is the difference between map(), filter(), and reduce()?</h3>
<p>map() applies a function to every item in an iterable, filter() selects items that satisfy a condition, and reduce() combines items into a single result. reduce() is available from functools.</p>

<pre><code>from functools import reduce

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda a, b: a + b, nums))
</code></pre>

<h3>29. What are exceptions in Python? How do we handle them?</h3>
<p>Exceptions are runtime errors that interrupt program execution. They are handled with try, except, and finally blocks to prevent the program from crashing.</p>

<pre><code>try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")
</code></pre>

<h3>30. What is object-oriented programming (OOP)? Explain classes, objects, inheritance, and polymorphism.</h3>
<p>OOP is a programming style that organizes code into classes and objects. A class is a blueprint, an object is an instance of a class, inheritance allows one class to reuse features of another, and polymorphism allows the same method to behave differently in different classes.</p>

<pre><code>class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

obj = Dog()
obj.speak()
</code></pre>

<h2>Extra Advanced Questions</h2>

<h3>What is the difference between instance method, class method, and static method?</h3>
<p>An instance method works with an object instance, a class method works with the class itself, and a static method does not depend on the instance or class. They are defined using @classmethod and @staticmethod.</p>

<h3>What is __init__ in Python classes?</h3>
<p>__init__ is a special method called automatically when an object is created. It initializes the object’s attributes.</p>

<h3>What is the difference between shallow copy and deep copy?</h3>
<p>A shallow copy creates a new object but references the same nested objects. A deep copy creates a new copy of the nested objects as well. This is important when working with nested lists or dictionaries.</p>

<h3>What are iterators and generators?</h3>
<p>An iterator is an object that can be iterated over, while a generator is a function that yields values one at a time, saving memory for large datasets.</p>

<h3>What is the use of *args and **kwargs?</h3>
<p>*args allows a function to accept a variable number of positional arguments, and **kwargs allows it to accept a variable number of keyword arguments.</p>

<h3>What are decorators in Python?</h3>
<p>Decorators are used to modify or enhance functions or methods without changing their source code. They are often used for logging, access control, and performance tracking.</p>

<h3>What is the difference between local and global variables?</h3>
<p>A local variable is defined inside a function and is accessible only there. A global variable is defined outside a function and can be used across the program.</p>

<h3>What is method overriding?</h3>
<p>Method overriding happens when a child class defines a method that already exists in its parent class. The child version is used when the method is called on the child object.</p>

<h3>What is encapsulation, abstraction, and inheritance?</h3>
<p>Encapsulation hides internal details of an object, abstraction focuses on essential features while ignoring implementation details, and inheritance allows a class to reuse methods and attributes from another class.</p>

<h3>What is a module in Python?</h3>
<p>A module is a Python file containing reusable code. It can be imported using the import keyword to use functions, classes, and variables defined elsewhere.</p>

<h3>Tips for interview preparation</h3>
<p>To prepare well for a Python interview, practice basic syntax, data structures, loops, functions, recursion, OOP, and exception handling. Also, write small code snippets and explain them clearly during the interview.</p>
