# Write a recursive function to calculate the sum of first n natural numbers.

def  Natural_sum(num):
    if num == 0:
        return 0
    else:
        return num + Natural_sum(num-1)

num = int(input("Enter the natural number upto which u required sum : "))
sum = Natural_sum(num)
print(sum)


# Write a recursive function to print all elements in a list.(hint: use list & index as parameters)

def print_lst(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx], end=" ")
    print_lst(list,idx+1)

fruits =["Mango","Banana","Lichi","Apple","Graps"]

print_lst(fruits)