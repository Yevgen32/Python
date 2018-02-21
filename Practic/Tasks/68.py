#Даны коэффициенты a,b,c уравнения ax2+bx+c=0. Найти решение. Проверить ответы можно здесь. Как решать квадратные уравнения можно прочитать здесь.

import math

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

d = b ** 2 - 4 * a * c

print("d:", "d = %.2f" % d)

if d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
if d < 0:
    print("not sqrt")
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
