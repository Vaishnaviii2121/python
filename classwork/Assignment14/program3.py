class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first Number :"))
        self.value2 = int(input("Enter second Number :"))

    def Addition(self):
        return self.value1 + self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        if self.value2 == 0:
            return "Division by zero is not allowed"
        return self.value1 /  self.value2

obj1 = Arithmatic()
obj2 = Arithmatic()

obj1.Accept()

print("Addition :",obj1.Addition())
print("Subtraction :",obj1.Subtraction())
print("Multiplication :",obj1.Multiplication())
print("Division :",obj1.Division())

print("----------------")

obj2.Accept()

print("Addition :",obj2.Addition())
print("Subtraction :",obj2.Subtraction())
print("Multiplication :",obj2.Multiplication())
print("Division :",obj2.Division())
