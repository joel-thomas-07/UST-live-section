class BankAccount:
    ROI =10.5
    def __init__(self,Name,amount):
        self.Name = Name
        self.amount=amount

    def display(self):
        print(f" Name is : {self.Name} \n Amount is :{self.amount}")

    def calcinterest(self):
        self.amount += (self.amount * BankAccount.ROI)/100
        print(f"Amount is {self.amount}")
    def deposit(self,Amount):
        if isinstance(Amount,int):
            if Amount >0:
                self.amount +=Amount
                print("deposit successful")
            else:
                print("failed to deposit")
        else:
            print("please enter a valid amount")

    def withdraw(self,Amount):
        if Amount<=self.amount:
            self.amount-=Amount
            print("withdraw successful")
        else:
            print("insufficient balance !!!")

B1=BankAccount("joel",23000)
B1.calcinterest()
B1.withdraw(100011)
B1.withdraw(1000)
B1.deposit(232)
B1.display()