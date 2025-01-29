import random
import string
from datetime import datetime, timedelta
import urllib.parse

class RandomExercise:
    def __init__(self):
        pass

    def generate_divisible_by_5(self):
        divisible_numbers = [random.randrange(100, 999, 5) for _ in range(3)]
        return divisible_numbers

    def lottery_tickets(self):
        tickets = random.sample(range(100000, 999999), 100)
        winners = random.sample(tickets, 2)
        return tickets, winners

    def generate_otp(self):
        return random.randint(100000, 999999)

    def random_character(self, input_string):
        return random.choice(input_string)

    def random_string(self):
        random_characters = random.choices(string.ascii_letters, k=5)
        return ''.join(random_characters)

    def generate_password(self):
        password_length = 10
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length - 4)
        random.shuffle(password)
        return ''.join(password)

    def multiply_random_floats(self):
        num1 = random.uniform(1.0, 10.0)
        num2 = random.uniform(1.0, 10.0)
        return num1, num2, num1 * num2

    def generate_token_and_url(self):
        secure_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        base_url = "https://www.example.com/"
        random_url = urllib.parse.urljoin(base_url, ''.join(random.choices(string.ascii_letters + string.digits, k=10)))
        return secure_token, random_url

    def roll_dice_fixed(self):
        random.seed(42)
        return random.choice([1, 2, 3, 4, 5, 6])

    def random_date_between(self, start_date, end_date):
        time_delta = end_date - start_date
        random_days = random.randint(0, time_delta.days)
        random_date = start_date + timedelta(days=random_days)
        return random_date.strftime("%Y-%m-%d")


exercise = RandomExercise()

print("1. Random divisible by 5:", exercise.generate_divisible_by_5())
print("2. Lottery winners:", exercise.lottery_tickets())
print("3. OTP:", exercise.generate_otp())
print("4. Random Character from String:", exercise.random_character("HelloParagSir"))
print("5. Random String:", exercise.random_string())
print("6. Generated Password:", exercise.generate_password())
num1, num2, result = exercise.multiply_random_floats()
print(f"7. Multiplication of {num1:.2f} and {num2:.2f} = {result:.2f}")
token, url = exercise.generate_token_and_url()
print("8. Secure Token:", token)
print("   Random URL:", url)
print("9. Fixed Dice Roll:", exercise.roll_dice_fixed())
print("10. Random Date:", exercise.random_date_between(datetime(2020, 1, 1), datetime(2025, 1, 1)))
