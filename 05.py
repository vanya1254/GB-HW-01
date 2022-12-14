# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance_between_dotes(x1, y1, x2, y2):
    return ((x2 -x1)**2 + (y2 - y1)**2)**0.5                # либо sqrt() решил не импортировать math


x_a = int(input("Enter X of first point --> "))
y_a = int(input("Enter Y of first point --> "))

x_b = int(input("Enter X of second point --> "))
y_b = int(input("Enter Y of second point --> "))

distance = round(distance_between_dotes(x_a, y_a, x_b, y_b), 2)
print(f"Distance between A({x_a}, {y_a}) and B({x_b}, {y_b}) = {distance}")