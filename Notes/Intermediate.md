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