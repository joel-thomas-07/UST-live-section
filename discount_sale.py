quant = int(input("Enter the quantity of items: "))
ppi = float(input("Enter price per item: "))
total = quant * ppi
gross_price = lambda quant, ppi:total - (0.1 * total if quant > 10 else 0)
print("Total Expenses: ", f"{gross_price(quant,ppi):.2f}")