#Даны три числа. Найдите те два из них, сумма которых наибольшая.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

b = x + y

if x + y < x + z:
    b = x + z
if b < z + y:
    b = z + y

print(b)
