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