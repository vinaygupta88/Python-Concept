# while loops
cnt = 0
while cnt < 3:
    print("Hello Vinay")
    cnt = cnt + 1

# for loop
n = 4
for i in range(0, n):
    print(i)


# index of sequence
a = ["geeks", "for", "geeks"]
for idx in range(len(a)):
    print(a[idx])

# nested loop

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()


# Print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in lst:
    print(el)

# Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 9
for el in tup:
    if(el==x):
        print(x,"Found")
        break;
else:
    print(x, " is not found")
