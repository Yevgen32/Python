#Пользователь вводит три числа - длины сторон треугольника. Найти площадь треугольника. Сделать проверку на существование треугольника (например, 1, 2, 3 - такого треугольника не существует). Проверить ответы можно здесь

import math

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) /2
    print("p:",p*2)
    s = (p * ( p - a ) * ( p - b ) * ( p - c ))**0.5
    print("s:",s)
    print("true")
else:
	print("false")

