class ShopCart:
    def __init__(self):
        self.items = [["bread", 40], ["cookie", 35], ["butter", 50], ["cheese", 60], ["yogurt", 20]]
        self.orderlist = []

    def ordering(self):
        item = input("Enter the item name: ").lower()
        for product in self.items:
            if product[0] == item:
                quant = int(input("Enter quantity: "))
                for order in self.orderlist:
                    if order[0] == item:
                        order[1] += quant
                        break
                else:
                    self.orderlist.append([item, quant])
                return
        print(item, "is not available.")

    def update(self):
        item = input("Enter the item name: ").lower()
        for order in self.orderlist:
            if order[0] == item:
                quant = int(input("Enter new quantity: "))
                order[1] = quant
                print(item, "updated in your cart.")
                return
        print("Item not in your list.")

    def delete(self):
        item = input("Enter the item name: ").lower()
        for i, order in enumerate(self.orderlist):
            if order[0] == item:
                del self.orderlist[i]
                print(item, "removed from your cart.")
                return
        print(item, "is not in your order list.")

    def billing(self):
        sumi = 0
        if not self.orderlist:
            print("Your cart is empty.")
        else:
            print("Item  Quantity  Price  Total")
            for order in self.orderlist:
                item_name = order[0]
                quant = order[1]
                for product in self.items:
                    if product[0] == item_name:
                        total = quant * product[1]
                        print(f"{item_name.capitalize()}   {quant}       {product[1]}     {total}")
                        sumi += total
                        break
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
                for product in self.items:
                    print(f"{product[0].capitalize()}: {product[1]}")
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
