#Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
print("Введите координаты точки x1= ")
x1 = float(input())
print("Введите координаты точки х2= ")
x2 = float(input())
print("Введите координаты точки y1= ")
y1 = float(input())
print("Введите координаты точки y2= ")
y2 = float(input())
from math import sqrt
otrezok = round(sqrt((x2 - x1)**2 + (y2 - y1)**2))
print("Расстояние между точками равно : ",otrezok)