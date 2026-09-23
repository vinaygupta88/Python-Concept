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

<h2>Additional Questions Frequently Asked in Interviews or Exams</h2>

<h3>31. What is a keyword in Python? Give some examples.</h3>
<p>A keyword is a reserved word in Python that has a special meaning and cannot be used as an identifier. Examples: if, else, for, while, def, class, return, True, False, None.</p>

<h3>32. What is the difference between is and == in Python?</h3>
<p>The == operator compares values, while is compares object identity. Two variables may have the same value but different memory references.</p>

<pre><code>a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True
print(a is b)   # False
</code></pre>

<h3>33. What is mutable and immutable data type?</h3>
<p>Mutable objects can be modified after creation, such as lists and dictionaries. Immutable objects cannot be changed once created, such as strings, tuples, and integers.</p>

<h3>34. What is the difference between list() and tuple() conversion?</h3>
<p>list() converts any iterable into a list, while tuple() converts it into a tuple. Lists are mutable, tuples are immutable.</p>

<pre><code>s = "abc"
print(list(s))
print(tuple(s))
</code></pre>

<h3>35. What is the purpose of the split() method?</h3>
<p>The split() method breaks a string into a list of substrings based on a separator. By default, it splits on whitespace.</p>

<pre><code>text = "Python is easy"
print(text.split())
</code></pre>

<h3>36. What is the difference between split() and join()?</h3>
<p>split() converts a string into a list, while join() converts a list of strings into a single string.</p>

<pre><code>words = ["Python", "is", "easy"]
print(" ".join(words))
</code></pre>

<h3>37. What is the difference between append() and extend() for a list?</h3>
<p>append() adds one element as a single item, while extend() adds multiple elements from another iterable.</p>

<h3>38. What is a nested loop?</h3>
<p>A nested loop is a loop inside another loop. It is commonly used to work with matrices or multi-dimensional data.</p>

<pre><code>for i in range(3):
    for j in range(2):
        print(i, j)
</code></pre>

<h3>39. What is the difference between local variable and global variable?</h3>
<p>A local variable is declared inside a function and can be used only there. A global variable is declared outside any function and can be accessed throughout the program.</p>

<pre><code>x = 10

def show():
    y = 20
    print(x, y)
</code></pre>

<h3>40. What is the purpose of the return statement?</h3>
<p>The return statement ends a function and sends a result back to the caller. Without return, a function returns None.</p>

<pre><code>def square(n):
    return n * n
</code></pre>

<h3>41. What is the difference between a function and a method?</h3>
<p>A function is a standalone block of code, while a method is a function defined inside a class and called on an object.</p>

<h3>42. What is a module in Python? How do you import it?</h3>
<p>A module is a Python file that contains functions, classes, or variables. It is imported using the import statement.</p>

<pre><code>import math
print(math.sqrt(16))
</code></pre>

<h3>43. What is the purpose of the len() function?</h3>
<p>The len() function returns the length of a string, list, tuple, dictionary, or set.</p>

<pre><code>print(len("Python"))
print(len([1, 2, 3]))
</code></pre>

<h3>44. What is the difference between sorted() and sort()?</h3>
<p>sort() sorts a list in place, while sorted() returns a new sorted list without changing the original list.</p>

<pre><code>nums = [5, 2, 8]
print(sorted(nums))
print(nums)
nums.sort()
print(nums)
</code></pre>

<h3>45. What is a dictionary key and value?</h3>
<p>A dictionary stores data as key-value pairs. Keys are unique identifiers, and values are the data associated with those keys.</p>

<pre><code>student = {"name": "Rahul", "age": 22}
print(student["name"])
</code></pre>

<h3>46. What is the difference between a set and a frozenset?</h3>
<p>A set is mutable, meaning elements can be added or removed. A frozenset is immutable and cannot be changed after creation.</p>

<h3>47. What do you mean by list comprehension?</h3>
<p>List comprehension is a compact way to create a list using a single line of code.</p>

<pre><code>squares = [x * x for x in range(1, 6)]
print(squares)
</code></pre>

<h3>48. What is the difference between / and // operators?</h3>
<p>/ returns a floating-point result, while // performs floor division and returns the integer quotient.</p>

<pre><code>print(9 / 2)   # 4.5
print(9 // 2)  # 4
</code></pre>

<h3>49. What is the difference between and and or operators?</h3>
<p>and returns True only if both conditions are true. or returns True if at least one condition is true.</p>

<pre><code>a = True
b = False
print(a and b)
print(a or b)
</code></pre>

<h3>50. What is the difference between index and value in a list?</h3>
<p>An index is the position of an element in a list, starting from 0. A value is the actual stored data in that position.</p>

<pre><code>lst = [10, 20, 30]
print(lst[0])  # value 10 at index 0
</code></pre>

<h3>51. What are Python comments?</h3>
<p>Comments are non-executable lines used to explain the code. They help other developers understand the logic. Python uses # for single-line comments.</p>

<pre><code># This is a comment
print("Hello")
</code></pre>

<h3>52. What is the difference between tuple unpacking and list unpacking?</h3>
<p>Tuple unpacking and list unpacking both extract values from sequences. The main difference is that tuples are immutable, while lists are mutable.</p>

<pre><code>a, b = (10, 20)
print(a, b)
</code></pre>

<h3>53. What is an exception in Python?</h3>
<p>An exception is an error that occurs during program execution, such as dividing by zero or using an invalid index. Exceptions can be handled using try, except, and finally.</p>

<h3>54. What is the difference between a syntax error and an exception?</h3>
<p>A syntax error occurs when the code is written incorrectly and cannot be parsed. An exception occurs while the program is running and can sometimes be handled.</p>

<h3>55. What is the purpose of the finally block?</h3>
<p>The finally block always executes whether an error occurs or not. It is used to clean up resources such as closing files.</p>

<pre><code>try:
    x = 1
except:
    print("Error")
finally:
    print("Cleanup")
</code></pre>

<h3>56. What is the difference between a list and a string in terms of mutability?</h3>
<p>A list is mutable and can be changed after creation, while a string is immutable and cannot be changed once created.</p>

<h3>57. What is a dictionary method get() used for?</h3>
<p>The get() method is used to access a dictionary value by key without raising a KeyError when the key is missing.</p>

<pre><code>d = {"name": "Riya"}
print(d.get("name"))
print(d.get("age", "Not found"))
</code></pre>

<h3>58. What is the difference between set.add() and set.update()?</h3>
<p>add() adds a single element to a set, while update() adds multiple elements or another iterable.</p>

<pre><code>s = {1, 2}
s.add(3)
s.update([4, 5])
print(s)
</code></pre>

<h3>59. What is a palindrome?</h3>
<p>A palindrome is a string or number that reads the same forward and backward. Example: "madam", "121".</p>

<pre><code>text = "madam"
print(text == text[::-1])
</code></pre>

<h3>60. What is the difference between recursion and iteration?</h3>
<p>Recursion uses function calls to solve a problem, while iteration uses loops. Recursion is usually more elegant for tree or factorial problems, but loops may be more efficient and easier to understand.</p>

<h3>61. What is a class in Python?</h3>
<p>A class is a blueprint for creating objects. It defines attributes and methods that the objects of that class can use.</p>

<pre><code>class Student:
    def __init__(self, name):
        self.name = name
</code></pre>

<h3>62. What is an object in Python?</h3>
<p>An object is an instance of a class. It contains data and can use the methods defined in the class.</p>

<pre><code>s1 = Student("Rahul")
print(s1.name)
</code></pre>

<h3>63. What is inheritance in Python?</h3>
<p>Inheritance allows a class to reuse attributes and methods from another class. The child class inherits from the parent class.</p>

<pre><code>class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    pass
</code></pre>

<h3>64. What is polymorphism?</h3>
<p>Polymorphism means the same method name can behave differently depending on the object using it. For example, different classes may implement speak() in different ways.</p>

<h3>65. What is the purpose of __str__() in a class?</h3>
<p>__str__() defines how an object should be represented as a string when printed.</p>

<pre><code>class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
</code></pre>

<h3>66. What is the difference between private and public variables in Python?</h3>
<p>Public variables can be accessed from anywhere, while private variables are intended to be used only inside the class and are often prefixed with _ or __.</p>

<h3>67. What is the use of the collections module?</h3>
<p>The collections module provides special data structures like defaultdict, Counter, deque, and OrderedDict that are useful in many programming problems.</p>

<pre><code>from collections import Counter
print(Counter([1, 2, 2, 3]))
</code></pre>

<h3>68. What is the difference between a list and a deque?</h3>
<p>A list supports indexing and is good for general use, while a deque from collections is optimized for fast append and pop operations from both ends.</p>

<h3>69. What are the advantages of Python?</h3>
<p>Python is easy to learn, has a clean syntax, supports rapid development, has a large library ecosystem, and is useful for automation, web development, data science, AI, and scripting.</p>

<h3>70. What are the disadvantages of Python?</h3>
<p>Python can be slower than lower-level languages like C and C++, and it may use more memory in some cases. It is not always the best choice for very high-performance or system-level programming.</p>

<h3>Final Revision Tip</h3>
<p>For interviews and exams, focus on core topics like Python syntax, variables, loops, functions, strings, lists, dictionaries, sets, OOP, recursion, and exception handling. Writing and explaining small code examples will help you answer confidently.</p>

<h2>Coding Questions (Basic to Advanced)</h2>

<h3>1. Write a Python program to add two numbers entered by the user.</h3>
<pre><code>a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
</code></pre>

<h3>2. Write a program to check whether a number is even or odd.</h3>
<pre><code>n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
</code></pre>

<h3>3. Write a program to find the greatest of three numbers.</h3>
<pre><code>a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest is", a)
elif b >= a and b >= c:
    print("Greatest is", b)
else:
    print("Greatest is", c)
</code></pre>

<h3>4. Write a program to print the first 10 natural numbers.</h3>
<pre><code>for i in range(1, 11):
    print(i)
</code></pre>

<h3>5. Write a program to calculate the factorial of a number.</h3>
<pre><code>n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)
</code></pre>

<h3>6. Write a Python program to check whether a number is prime or not.</h3>
<pre><code>n = int(input("Enter a number: "))
flag = True

if n <= 1:
    flag = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break

if flag:
    print("Prime")
else:
    print("Not Prime")
</code></pre>

<h3>7. Write a program to reverse a string.</h3>
<pre><code>s = input("Enter a string: ")
print(s[::-1])
</code></pre>

<h3>8. Write a program to count vowels in a string.</h3>
<pre><code>s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowels:", count)
</code></pre>

<h3>9. Write a program to find the sum of elements in a list.</h3>
<pre><code>nums = [10, 20, 30, 40]
print(sum(nums))
</code></pre>

<h3>10. Write a program to find the largest number in a list.</h3>
<pre><code>nums = [12, 45, 7, 89, 23]
print(max(nums))
</code></pre>

<h3>11. Write a program to remove duplicate values from a list.</h3>
<pre><code>nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)
</code></pre>

<h3>12. Write a program to print a multiplication table of a number.</h3>
<pre><code>n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
</code></pre>

<h3>13. Write a program to check if a string is a palindrome.</h3>
<pre><code>s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
</code></pre>

<h3>14. Write a program to sort a list in ascending order.</h3>
<pre><code>nums = [9, 1, 7, 2, 5]
nums.sort()
print(nums)
</code></pre>

<h3>15. Write a program to count the frequency of each element in a list.</h3>
<pre><code>nums = [1, 2, 2, 3, 3, 3, 4]
count = {}
for n in nums:
    count[n] = count.get(n, 0) + 1
print(count)
</code></pre>

<h3>16. Write a program to check if a number is a perfect square.</h3>
<pre><code>n = int(input("Enter a number: "))
root = int(n ** 0.5)
if root * root == n:
    print("Perfect square")
else:
    print("Not a perfect square")
</code></pre>

<h3>17. Write a program to print the Fibonacci series up to n terms.</h3>
<pre><code>n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
</code></pre>

<h3>18. Write a program to find the sum of first n natural numbers using a while loop.</h3>
<pre><code>n = int(input("Enter n: "))
sum_val = 0
count = 1
while count <= n:
    sum_val += count
    count += 1
print(sum_val)
</code></pre>

<h3>19. Write a program to create a dictionary of student names and marks.</h3>
<pre><code>students = {
    "Amit": 85,
    "Neha": 90,
    "Raj": 78
}
print(students)
</code></pre>

<h3>20. Write a program to swap two numbers without using a third variable.</h3>
<pre><code>a = 10
b = 20
a, b = b, a
print(a, b)
</code></pre>

<h3>21. Write a program to find the factorial of a number using recursion.</h3>
<pre><code>def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
</code></pre>

<h3>22. Write a recursive function to print all elements of a list.</h3>
<pre><code>def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

print_list([10, 20, 30, 40])
</code></pre>

<h3>23. Write a program to check if a list is empty or not.</h3>
<pre><code>lst = []
if not lst:
    print("List is empty")
else:
    print("List is not empty")
</code></pre>

<h3>24. Write a program to merge two dictionaries.</h3>
<pre><code>d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)
</code></pre>

<h3>25. Write a program to remove all spaces from a string.</h3>
<pre><code>s = "P y t h o n"
print(s.replace(" ", ""))
</code></pre>

<h3>26. Write a program to find the common elements between two lists.</h3>
<pre><code>list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]
print(common)
</code></pre>

<h3>27. Write a program to calculate the average of numbers in a list.</h3>
<pre><code>nums = [10, 20, 30, 40]
avg = sum(nums) / len(nums)
print(avg)
</code></pre>

<h3>28. Write a program to print the pattern:</h3>
<pre><code>*
**
***
****
*****
</code></pre>
<pre><code>for i in range(1, 6):
    print('*' * i)
</code></pre>

<h3>29. Write a program to check if a year is a leap year.</h3>
<pre><code>year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
</code></pre>

<h3>30. Write a program to find the second largest number in a list.</h3>
<pre><code>nums = [12, 45, 7, 89, 23]
nums = sorted(set(nums))
print(nums[-2])
</code></pre>

<h3>31. Write a program to input a sentence and count words.</h3>
<pre><code>sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))
</code></pre>

<h3>32. Write a program to check whether a string contains a substring.</h3>
<pre><code>text = "Python programming"
sub = "program"
if sub in text:
    print("Found")
else:
    print("Not found")
</code></pre>

<h3>33. Write a program to find the sum of digits of a number.</h3>
<pre><code>n = int(input("Enter a number: "))
num = n
s = 0
while num > 0:
    s += num % 10
    num //= 10
print("Sum of digits:", s)
</code></pre>

<h3>34. Write a program to print all even numbers from 1 to 50.</h3>
<pre><code>for i in range(1, 51):
    if i % 2 == 0:
        print(i)
</code></pre>

<h3>35. Write a program to create a calculator using functions.</h3>
<pre><code>def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add(5, 3))
print(sub(5, 3))
print(mul(5, 3))
print(div(5, 3))
</code></pre>

<h3>36. Write a program to check whether a string is uppercase, lowercase, or mixed.</h3>
<pre><code>s = input("Enter a string: ")
if s.isupper():
    print("Uppercase")
elif s.islower():
    print("Lowercase")
else:
    print("Mixed")
</code></pre>

<h3>37. Write a program to remove vowels from a string.</h3>
<pre><code>s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = "".join(ch for ch in s if ch not in vowels)
print(result)
</code></pre>

<h3>38. Write a program to find the number of uppercase letters in a string.</h3>
<pre><code>s = input("Enter a string: ")
count = sum(1 for ch in s if ch.isupper())
print(count)
</code></pre>

<h3>39. Write a program to implement a simple login system using dictionary.</h3>
<pre><code>users = {"admin": "1234", "user": "pass"}
name = input("Enter username: ")
password = input("Enter password: ")
if users.get(name) == password:
    print("Login successful")
else:
    print("Invalid username or password")
</code></pre>

<h3>40. Write a program to reverse each word in a sentence.</h3>
<pre><code>sentence = input("Enter a sentence: ")
words = sentence.split()
rev_words = [word[::-1] for word in words]
print(" ".join(rev_words))
</code></pre>

<h3>41. Write a program to find the sum of numbers in a 2D list.</h3>
<pre><code>matrix = [[1, 2], [3, 4], [5, 6]]
print(sum(sum(row) for row in matrix))
</code></pre>

<h3>42. Write a program to find the transpose of a matrix.</h3>
<pre><code>matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(transpose)
</code></pre>

<h3>43. Write a program to implement linear search.</h3>
<pre><code>nums = [10, 20, 30, 40, 50]
key = 30
found = False
for i in range(len(nums)):
    if nums[i] == key:
        print("Found at index", i)
        found = True
        break
if not found:
    print("Not found")
</code></pre>

<h3>44. Write a program to implement binary search.</h3>
<pre><code>nums = [10, 20, 30, 40, 50]
key = 30
low, high = 0, len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == key:
        print("Found at index", mid)
        break
    elif nums[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
</code></pre>

<h3>45. Write a program to find the HCF of two numbers.</h3>
<pre><code>a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b
print("HCF:", a)
</code></pre>

<h3>46. Write a program to find the LCM of two numbers.</h3>
<pre><code>a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while x != y:
    if x < y:
        x += a
    else:
        y += b
print("LCM:", x)
</code></pre>

<h3>47. Write a program to print the ASCII value of a character.</h3>
<pre><code>ch = input("Enter a character: ")
print(ord(ch))
</code></pre>

<h3>48. Write a program to check if a string is an anagram.</h3>
<pre><code>s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(sorted(s1) == sorted(s2))
</code></pre>

<h3>49. Write a program to count the number of digits in a number.</h3>
<pre><code>n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits:", count)
</code></pre>

<h3>50. Write a program to print the reverse of a list without using slicing.</h3>
<pre><code>nums = [1, 2, 3, 4, 5]
rev = []
for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])
print(rev)
</code></pre>

<h3>51. Write a Python program using a function to check if a number is prime.</h3>
<pre><code>def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
</code></pre>

<h3>52. Write a program to check if a string contains only digits.</h3>
<pre><code>s = input("Enter a string: ")
print(s.isdigit())
</code></pre>

<h3>53. Write a program to remove duplicate characters from a string.</h3>
<pre><code>s = "programming"
result = "".join(dict.fromkeys(s))
print(result)
</code></pre>

<h3>54. Write a program to find the longest word in a sentence.</h3>
<pre><code>sentence = input("Enter a sentence: ")
words = sentence.split()
print(max(words, key=len))
</code></pre>

<h3>55. Write a program to read a list of numbers and print only the odd numbers.</h3>
<pre><code>nums = [1, 2, 3, 4, 5, 6, 7]
print([n for n in nums if n % 2 != 0])
</code></pre>

<h3>56. Write a Python program to create a class Employee with attributes name and salary.</h3>
<pre><code>class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

emp = Employee("Ravi", 25000)
emp.display()
</code></pre>

<h3>57. Write a program to implement inheritance with a parent class and child class.</h3>
<pre><code>class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()
obj.speak()
obj.bark()
</code></pre>

<h3>58. Write a program to handle division by zero using exception handling.</h3>
<pre><code>try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")
</code></pre>

<h3>59. Write a program to print a star triangle in reverse order.</h3>
<pre><code>for i in range(5, 0, -1):
    print('*' * i)
</code></pre>

<h3>60. Write a program to find the most repeated element in a list.</h3>
<pre><code>nums = [1, 2, 3, 2, 2, 4, 5]
print(max(set(nums), key=nums.count))
</code></pre>

<h3>61. Write a program to convert a list of strings to uppercase.</h3>
<pre><code>names = ["vinay", "amit", "neha"]
print([name.upper() for name in names])
</code></pre>

<h3>62. Write a program to find the number of repeated letters in a word.</h3>
<pre><code>word = "banana"
count = {}
for ch in word:
    count[ch] = count.get(ch, 0) + 1
print(count)
</code></pre>

<h3>63. Write a program to print the sum of even numbers from 1 to 100.</h3>
<pre><code>total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)
</code></pre>

<h3>64. Write a program to count uppercase and lowercase letters in a string.</h3>
<pre><code>s = input("Enter a string: ")
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)
</code></pre>

<h3>65. Write a program to sort a dictionary by keys.</h3>
<pre><code>student = {"b": 2, "a": 1, "c": 3}
print(dict(sorted(student.items())))
</code></pre>

<h3>66. Write a program to generate a list of square numbers from 1 to 10.</h3>
<pre><code>squares = [x * x for x in range(1, 11)]
print(squares)
</code></pre>

<h3>67. Write a program to print the first n odd numbers.</h3>
<pre><code>n = int(input("Enter n: "))
for i in range(1, 2 * n, 2):
    print(i)
</code></pre>

<h3>68. Write a program to check if a number is Armstrong number.</h3>
<pre><code>num = int(input("Enter a number: "))
original = num
sum_val = 0
while num > 0:
    digit = num % 10
    sum_val += digit ** 3
    num //= 10
if sum_val == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
</code></pre>

<h3>69. Write a program to print the pattern of numbers:</h3>
<pre><code>1
12
123
1234
12345
</code></pre>
<pre><code>for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
</code></pre>

<h3>70. Write a program to find unique elements in a list.</h3>
<pre><code>nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)
</code></pre>

<h3>Final Coding Practice Tip</h3>
<p>Practice coding questions every day by writing small programs for loops, strings, lists, dictionaries, recursion, and classes. In interviews, focus on clean logic, correct syntax, and explaining your code step by step.</p>

<h2>Pattern Coding Questions</h2>

<h3>1. Write a program to print the pattern:</h3>
<pre><code>*
**
***
****
*****
</code></pre>
<pre><code>for i in range(1, 6):
    print('*' * i)
</code></pre>

<h3>2. Write a program to print the pattern:</h3>
<pre><code>*****
****
***
**
*
</code></pre>
<pre><code>for i in range(5, 0, -1):
    print('*' * i)
</code></pre>

<h3>3. Write a program to print the pattern:</h3>
<pre><code>    *
   **
  ***
 ****
*****
</code></pre>
<pre><code>for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
</code></pre>

<h3>4. Write a program to print the pattern:</h3>
<pre><code>*****
 ****
  ***
   **
    *
</code></pre>
<pre><code>for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)
</code></pre>

<h3>5. Write a program to print the pattern:</h3>
<pre><code>1
12
123
1234
12345
</code></pre>
<pre><code>for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
</code></pre>

<h3>Pattern Practice Tip</h3>
<p>Pattern programs are common in Python interviews because they test loop logic, spacing, and nested loop understanding. Practice them by focusing on how rows and columns are controlled.</p>

<h2>MCQ + Coding Mixed Practice</h2>

<h3>Multiple Choice Questions</h3>

<h4>1. Which of the following is a Python keyword?</h4>
<p>a) name<br>
b) for<br>c) value<br>d) x</p>
<p><b>Answer:</b> b) for</p>

<h4>2. Which data type is used to store key-value pairs?</h4>
<p>a) List<br>b) Tuple<br>c) Dictionary<br>d) Set</p>
<p><b>Answer:</b> c) Dictionary</p>

<h4>3. What is the output of print(9 // 2)?</h4>
<p>a) 4.5<br>b) 4<br>c) 5<br>d) 2</p>
<p><b>Answer:</b> b) 4</p>

<h4>4. Strings in Python are:</h4>
<p>a) Mutable<br>b) Immutable<br>c) Static<br>d) None</p>
<p><b>Answer:</b> b) Immutable</p>

<h4>5. Which function is used to get user input?</h4>
<p>a) input()<br>b) read()<br>c) scan()<br>d) get()</p>
<p><b>Answer:</b> a) input()</p>

<h4>6. Which of the following is a mutable data type?</h4>
<p>a) Tuple<br>b) String<br>c) List<br>d) Integer</p>
<p><b>Answer:</b> c) List</p>

<h4>7. What does range(5) generate?</h4>
<p>a) 0 to 5<br>b) 1 to 5<br>c) 0 to 4<br>d) 1 to 4</p>
<p><b>Answer:</b> c) 0 to 4</p>

<h4>8. Which symbol is used for comments in Python?</h4>
<p>a) // <br>b) /* */<br>c) #<br>d) --</p>
<p><b>Answer:</b> c) #</p>

<h4>9. Which of the following is used to define a function?</h4>
<p>a) define<br>b) func<br>c) def<br>d) function</p>
<p><b>Answer:</b> c) def</p>

<h4>10. Which of the following is used to create an empty set?</h4>
<p>a) {}<br>b) []<br>c) ()<br>d) set()</p>
<p><b>Answer:</b> d) set()</p>

<h4>11. What is the syntax for slicing a string?</h4>
<p>a) str[start:end]<br>b) str(start,end)<br>c) str{start:end}<br>d) str[start,end]</p>
<p><b>Answer:</b> a) str[start:end]</p>

<h4>12. Which operator is used for exponentiation?</h4>
<p>a) *<br>b) **<br>c) ^<br>d) %</p>
<p><b>Answer:</b> b) **</p>

<h4>13. What is the output of print("Python"[0])?</h4>
<p>a) y<br>b) P<br>c) n<br>d) o</p>
<p><b>Answer:</b> b) P</p>

<h4>14. Which method removes the last item from a list?</h4>
<p>a) remove()<br>b) clear()<br>c) pop()<br>d) del</p>
<p><b>Answer:</b> c) pop()</p>

<h4>15. What is used to handle exceptions in Python?</h4>
<p>a) if/else<br>b) try/except<br>c) while/for<br>d) def/class</p>
<p><b>Answer:</b> b) try/except</p>

<h4>16. Which of the following creates a tuple?</h4>
<p>a) [1, 2, 3]<br>b) {1, 2, 3}<br>c) (1, 2, 3)<br>d) {"1", "2"}</p>
<p><b>Answer:</b> c) (1, 2, 3)</p>

<h4>17. Which method converts a list into a set?</h4>
<p>a) list()<br>b) tuple()<br>c) set()<br>d) dict()</p>
<p><b>Answer:</b> c) set()</p>

<h4>18. What is recursion?</h4>
<p>a) Repeating code with loops<br>b) A function calling itself<br>c) A class inside a function<br>d) None of the above</p>
<p><b>Answer:</b> b) A function calling itself</p>

<h4>19. Which keyword is used to create a class?</h4>
<p>a) function<br>b) define<br>c) class<br>d) object</p>
<p><b>Answer:</b> c) class</p>

<h4>20. Which statement is used to skip the current loop iteration?</h4>
<p>a) break<br>b) pass<br>c) continue<br>d) return</p>
<p><b>Answer:</b> c) continue</p>

<h3>Coding Questions</h3>

<h4>1. Write a program to print the sum of two numbers.</h4>
<pre><code>a = 10
b = 20
print(a + b)
</code></pre>

<h4>2. Write a program to check whether a number is positive, negative or zero.</h4>
<pre><code>n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
</code></pre>

<h4>3. Write a program to print the first 20 even numbers.</h4>
<pre><code>count = 0
num = 2
while count < 20:
    print(num, end=" ")
    num += 2
    count += 1
</code></pre>

<h4>4. Write a program to reverse a number.</h4>
<pre><code>n = int(input("Enter a number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
</code></pre>

<h4>5. Write a program to count the number of characters in a string.</h4>
<pre><code>s = "Python"
print(len(s))
</code></pre>

<h4>6. Write a program to find the factorial of a number using recursion.</h4>
<pre><code>def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))
</code></pre>

<h4>7. Write a program to merge two lists.</h4>
<pre><code>a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
</code></pre>

<h4>8. Write a program to print the multiplication table of 5.</h4>
<pre><code>for i in range(1, 11):
    print(5 * i)
</code></pre>

<h4>9. Write a program to find the maximum value in a dictionary.</h4>
<pre><code>d = {"a": 10, "b": 25, "c": 18}
print(max(d.values()))
</code></pre>

<h4>10. Write a program to check if a string is palindrome.</h4>
<pre><code>s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
</code></pre>

<h4>11. Write a program to print the pattern:</h4>
<pre><code>1
22
333
4444
55555
</code></pre>
<pre><code>for i in range(1, 6):
    print(str(i) * i)
</code></pre>

<h4>12. Write a program to remove duplicate numbers from a list.</h4>
<pre><code>nums = [1, 2, 2, 3, 4, 4, 5]
print(list(set(nums)))
</code></pre>

<h3>Quick Revision Note</h3>
<p>For MCQ rounds, focus on Python basics, loops, functions, data types, and OOP. For coding rounds, practice loops, strings, lists, dictionaries, recursion, and pattern programs.</p>
