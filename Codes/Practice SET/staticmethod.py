# using static method design simple calculator
 
class Calc:
    @staticmethod           # @staticmethod: Declares the method as static
    def add(a, b):
        return a + b

res = Calc.add(2, 3)        # Normal function arguments (no self or cls)
print(res)