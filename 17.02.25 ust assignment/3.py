class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = None
        self.Area = None
        self.Circumference = None

    def Accept(self):
        self.Radius = int(input("Enter the radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius ** 2

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("RADIUS: ", self.Radius)
        print("AREA: ", self.Area)
        print("CIRCUMFERENCE: ", self.Circumference)


o1 = Circle()
o1.Accept()
o1.CalculateArea()
o1.CalculateCircumference()
o1.Display()