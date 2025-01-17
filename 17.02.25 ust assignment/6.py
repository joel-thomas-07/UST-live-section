class Arithmetic:
    def __init__(self):
        value1=None
        value2=None
    def Accept(self,val1,val2):
        self.value1=val1
        self.value2=val2
    def Addition(self):
        print(f" addition of {self.value1} and {self.value2} is {self.value1 + self.value2}")
    def Substraction(self):
        print(f" Substraction of {self.value1} and {self.value2} is {self.value1 - self.value2}")
    def Multiplication(self):
        print(f" Multiplication of {self.value1} and {self.value2} is {self.value1 * self.value2}")
    def Division(self):
        print(f" Division of {self.value1} and {self.value2} is {self.value1 / self.value2}")

Ar=Arithmetic()
Ar.Accept(25,5)
Ar.Addition()
Ar.Multiplication()
Ar.Division()
Ar.Substraction()