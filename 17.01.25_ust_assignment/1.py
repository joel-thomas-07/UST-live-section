class Demo:
    value = None

    def __init__(self, *val):
        self.val = val

    def Fun(self):
        print(self.val)
    def Gun(self):
        print(self.val)
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()