# Write a function to print the length of list(list is paramenter)
list = ['Delhi','Gurugram','Noida','Bengalru','Pune','Lucknow']

def print_lst(lst):
    for city in lst:
        print(city)

print_lst(list)

# Write a function to print the elements of a list in single line

def print_el(lst):
    for city in lst:
        print(city,end=" ")

print_el(list)


# Write a function to find the factorial of n (n is parameter)

def fact(n):
    factorial = 1
    for fct in range(1,n+1):
        factorial *= fct

    print(f'Factorial of {n} is {factorial}')

n = int(input("\nEnter the number: "))
fact(n)


## Recursion concepts