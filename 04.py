# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def print_range_quarter(quarter):
    if quarter == 1:
        print(f"Range {quarter} quarter = [x(0, +∞), y(0, +∞)]")
    elif quarter == 2:
        print(f"Range {quarter} quarter = [x(-∞, 0), y(0, +∞)]")
    elif quarter == 3:
        print(f"Range {quarter} quarter = [x(-∞, 0), y(-∞, 0)]")
    elif quarter == 4:
        print(f"Range {quarter} quarter = [x(0, +∞), y(-∞, 0)]")
    else:
        print("Enter number of quarter: 1, 2, 3, 4")

user_quarter = int(input("Enter number of quarter --> "))
print_range_quarter(user_quarter)