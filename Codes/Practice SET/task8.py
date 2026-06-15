#Create a new file "practice.txt" using python . Add the following data inn it-
#       Hi everyone 
#       we are learning File I/O
#       using Python
#       I like programming in Python

with open("practice.txt",'w') as f :
    f.write("Hi everyone\nWe are learning python\n")
    f.write("using python\nI like programming in python")

# Write a function that replace all occurance of "python" with "java" in above file.

with open("practice.txt",'r') as f:
    data = f.read()
new_data = data.replace("python", "Java")
print(new_data)

with open("practice.txt",'w') as f :
    f.write(new_data)


# Search if the word "learninng" exists in the file or not.
with open("practice.txt",'r') as f:
    data = f.read()
    if (data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")