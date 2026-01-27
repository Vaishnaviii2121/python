class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius of Circle :"))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius of circle :",self.Radius)
        print("Area of circle :",self.Area)
        print("Circumference",self.circumference)


cobj1 = Circle()
cobj2 = Circle()

cobj1.Accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()

print("---------------------------")

cobj2.Accept()
cobj2.CalculateArea()
cobj2.CalculateCircumference()
cobj2.Display()
        
