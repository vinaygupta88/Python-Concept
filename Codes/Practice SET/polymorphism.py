'''Inside the editor, complete the following steps:
Create a class Cat with a method sound that prints "Meow"
Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
Create objects c1 = Cat() and f1 = Fox()
Call sound() on both objects'''

# Create the Cat class
class Cat:
  def sound(self):
    print("Meow")

# Create the Fox class
class Fox:
  def sound(self):
    print("Wa-pa-pa-pa-pa-pow!")

# Create objects and loop
c1 = Cat()
f1 = Fox()

for animal in (c1, f1):
  animal.sound()
