class ShopCart:
    def __init__(self):
        self.items = {"bread": 40, "cookie": 35, "butter": 50, "cheese": 60, "yogurt": 20}
        self.orderlist = {}

    def ordering(self):
        item = input("Enter the item name: ").lower()
        if item in self.items:
            quant = int(input("Enter quantity: "))
            self.orderlist[item] = self.orderlist.get(item, 0) + quant
        else:
            print(item , " is not available.")

    def update(self):
        item = input("Enter the item name: ").lower()
        if item in self.orderlist:
            quant = int(input("Enter new quantity: "))
            self.orderlist[item] = quant
        else:
            print("Item not in your list.")

    def delete(self):
        item = input("Enter the item name: ").lower()
        if item in self.orderlist:
            self.orderlist.pop(item)
            print(item," removed from your cart.")
        else:
            print(item," is not in your order list.")


    def billing(self):
        sumi = 0
        if not self.orderlist:
            print("Your cart is empty.")
        else:
            print("Item  Quantity  Price  Total")
            for item, quant in self.orderlist.items():
                total = quant * self.items[item]
                print(f"{item.capitalize()}   {quant}       {self.items[item]}     {total}")
                sumi += total
            print(f"Total bill: {sumi}")

    def menu(self):
        while True:
            print("\nWhat do you want to do?")
            print("Enter 1 for viewing the available items")
            print("Enter 2 for adding items to the cart")
            print("Enter 3 for updating items in the cart")
            print("Enter 4 for deleting items from the cart")
            print("Enter 5 for printing the bill")
            print("Enter 6 to exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Available items:")
                for item, price in self.items.items():
                    print(item.capitalize(),":" ,price)
            elif choice == 2:
                self.ordering()
            elif choice == 3:
                self.update()
            elif choice == 4:
                self.delete()
            elif choice == 5:
                self.billing()
            elif choice == 6:
                print("Thank you for shopping!")
                break
            else:
                print("Wrong choice, please enter a correct option.")


c = ShopCart()
c.menu()
