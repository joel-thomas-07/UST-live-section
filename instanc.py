class Employee:
    family_name = "Manathundil "
    def __init__(self,name,age):
        self.name = name
        self.age=age
emp = Employee("joel",21)

print(isinstance(emp,Employee))
print(emp.name)
print (emp.age)