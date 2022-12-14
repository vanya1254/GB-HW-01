# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_right_num(user_num):
    days_num = [1, 2, 3, 4, 5, 6, 7]                        # задание простое, поэтому решил немного проверок добавить, чтобы самому интереснее было
    return user_num not in days_num 

condition = True
weekends = [6, 7]

while condition:
    day_num = int(input("Enter number of day --> "))
    condition = is_right_num(day_num)

if day_num in weekends:
    print(f"Yes {day_num} weekend")
else:
    print(f"{day_num} not weekend")