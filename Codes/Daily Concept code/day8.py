# 1. OPEN FILE IN READ MODE
file = open("sample.txt", "r")
print(file.read())
file.close()

# 2. OPEN FILE IN WRITE MODE (OVERWRITES CONTENT)
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()

# 3. OPEN FILE IN APPEND MODE
file = open("sample.txt", "a")
file.write("\nNew Line Added")
file.close()

# 4. CREATE NEW FILE USING x MODE
file = open("newfile.txt", "x")
file.close()

# 5. READ ENTIRE FILE
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 6. READ FIRST 10 CHARACTERS
with open("sample.txt", "r") as file:
    print(file.read(10))

# 7. READ ONE LINE
with open("sample.txt", "r") as file:
    print(file.readline())

# 8. READ ALL LINES AS LIST
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# 9. WRITE MULTIPLE LINES
with open("sample.txt", "w") as file:
    file.writelines([
        "Apple\n",
        "Banana\n",
        "Mango\n"
    ])


# 10. FILE PROPERTIES
with open("sample.txt", "r") as file:
    print("Name :", file.name)
    print("Mode :", file.mode)
    print("Closed :", file.closed)

# 11. EXCEPTION HANDLING
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File Not Found")


# 12. DELETE FILE
import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File Deleted")
else:
    print("File Not Found")

# 13. RENAME FILE
import os

os.rename("old.txt", "new.txt")


# 14. WRITE BINARY FILE
with open("binary.bin", "wb") as file:
    file.write(b"Hello World")

# 15. READ BINARY FILE
with open("binary.bin", "rb") as file:
    data = file.read()
    print(data)


# 16. CSV FILE WRITING
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Rahul"])
    writer.writerow([2, "Aman"])

# 21. JSON FILE WRITING
import json

student = {
    "id": 1,
    "name": "Rahul",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)