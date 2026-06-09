# List creation using square bracket
lst = []
print(type(lst))

# List creation using constructor
a = list((1, 2, 3, "apple", 4.5))
print(a)

# list Append
print("\nList Append Method")
ex = []
ex.append(5)
print(ex)

print("\nList insert Method")
ex.insert(2,10)
print(ex)

print("\nList extend Method")
ex.extend([23,30])
print(ex)

print("\nList Sort Method")
ex.sort()
print(ex)
ex.sort(reverse=True)
print(ex)

print("\nList concatenation")
lst1 = [1,5,2,4,6]
lst2 = [23,52,1,345]
print(lst1 + lst2)

print("\nList Slicing; ")
lst = list('Development')
print(lst[1:])
print(lst[::-1])
print(lst[4:9])

#Unpacking 
print("\nList Unpacking")
print(*lst1 ,*lst2)

# Tuple creation
print("\n\nTuple")
tup = ()
print(type(tup))

tup = (1,)
print(tup,"\n")

print("Tuple concatenation")
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

print("\nTuple Slicing; ")
tup = tuple('Development')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])