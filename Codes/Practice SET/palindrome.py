# Write to check if a list contains a palindrome of element.(Hint: used copy() method)

lst = ['M','A','D','A','M']
lst2 = [1,2,3]

lst_copy = lst.copy()
lst2_copy = lst2.copy()

lst.reverse()
lst2_copy.reverse()

if(lst_copy == lst ):
    print("Palindrome")
else:
    print("Not Palindrome")


print("\nSecond List")
if(lst2_copy == lst2 ):
    print("Palindrome")
else:
    print("Not Palindrome")