import random
lucky_number = int(input("Enter your lucky number (between 1 and 10): "))
while lucky_number < 1 or lucky_number > 10:
    lucky_number = int(input("Invalid input. Enter a number between 1 and 10: "))
while True:
    random_number = random.randint(1, 10)
    print(f"Generated number: {random_number}")
    if random_number == lucky_number:
        print("Congratulations! The random number matches your lucky number!")
        break
