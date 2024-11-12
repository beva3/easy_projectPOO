class Calculator:
    def __init__(self):
        print("Calculator ...")
        self.memory = 0
    def add(self,a,b):
        return a + b
    def substract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        try:
           return a/b
        except ZeroDivisionError:
           return "Error: Division by zero is not allowed."
    
    
    
c = Calculator()
print(c.add(3, 5))  # Output: 8
    
