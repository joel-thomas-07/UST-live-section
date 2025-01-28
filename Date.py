from datetime import datetime
from datetime import date, timedelta

date_input = input("Enter a date (DD/MM/YYYY): ")
date_obj = datetime.strptime(date_input, "%d/%m/%Y")

formatted_date = date_obj.strftime("%A %d %B %Y")
print("Formatted Date:", formatted_date)

day_of_week = date_obj.strftime("%A")
print("Day of the Week:", day_of_week)

new_date = date_obj + timedelta(days=15, hours=23)
print("New Date after adding 15 days and 23 hours:", new_date.strftime("%A %d %B %Y, %H:%M:%S"))

current_date = date.today()




def add_months(current_date, months):

    new_month = current_date.month + months
    new_year = current_date.year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1


    day = min(current_date.day, [31, 29 if new_year % 4 == 0 and (new_year % 100 != 0 or new_year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][new_month - 1])
    return date(new_year, new_month, day)


current_date = date.today()


date_in_6_months = add_months(current_date, 6)
print("Date 6 months from today:", date_in_6_months.strftime("%A %d %B %Y"))
