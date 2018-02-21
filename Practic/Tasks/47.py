#Даны три числа. Найдите наибольшее число из них.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

b = x

if x < y:
    b = y
if b < z:
    b = z

print(b)
