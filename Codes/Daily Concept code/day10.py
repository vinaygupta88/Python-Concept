## Methods with Parameters
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


# static method
class Calc:
    @staticmethod           # @staticmethod: Declares the method as static
    def add(a, b):
        return a + b

res = Calc.add(2, 3)        # Normal function arguments (no self or cls)
print(res)