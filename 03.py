# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Enter X --> "))
y = int(input("Enter Y --> "))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(f"({x}, {y}) in I quarter")
    elif x < 0 and y > 0:
        print(f"({x}, {y}) in II quarter")
    elif x < 0 and y < 0:
        print(f"({x}, {y}) in III quarter")
    elif x > 0 and y < 0:
        print(f"({x}, {y}) in IV quarter")
else:
    print("x != 0 y != 0, ok?")