#Даны катеты прямоугольного треугольника. Найдите площадь, периметр и гипотенузу треугольника.
import math

a = int(input("a:"))
b = int(input("b:"))

c = math.sqrt(a**2 + b**2)
s = 1/2 * (a*b)
p = a + b + c

print (s, "\t", c, "\t", p)
