def pow(x,n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)

class Main:
    def __init__(self):
        self.x = int(input("Enter number: "))
        self.n = int(input("Enter power: "))
        print("Result: ", pow(self.x,self.n))
A=Main()
