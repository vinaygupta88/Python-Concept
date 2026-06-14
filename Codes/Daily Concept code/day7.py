# square of each element
a = [2, 3, 4, 5]
res = [i ** 2 for i in a]
print(res)


# ODD EVEN using if else 
a = [1, 2, 3, 4, 5]
res = ['Even' if n % 2 == 0 else 'Odd' for n in a]
print(res)

## Lambda function

a = 'sangaButtapandu'
upper = lambda x: x.upper()  
print(upper(a))

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


## Generators
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a = sq_numbers(3)

print("The square of numbers 1, 2, 3 are:")
print(next(a))
print(next(a))
print(next(a))