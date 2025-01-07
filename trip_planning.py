def trip_calculator(km, lp, price):
    result = lambda km, lp, price: km / lp * price
    return result(km, lp, price)

km = int(input("How many km are you planning to travel: "))
price = int(input("Current price of petrol per litre: "))
lp = int(input("What is your mileage per litre: "))

print(f"Price for the entire trip is {trip_calculator(km, lp, price)}")
