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


# SET CONCEPT
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