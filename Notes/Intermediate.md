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