#Write a program to count the number of students with the "A" grade in the following tuple. ('C','D','A','A','B','B','A') Store the above values in a list & sort then from "A to D".

grade = ('C','D','A','A','B','B','A')

count = grade.count("A")
print(count)

lst = list(grade)
lst.sort()
print(lst)