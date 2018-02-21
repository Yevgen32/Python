#Даны три числа. Написать "yes", если среди них есть одинаковые.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x == y == z:
    print ("Yes")
if x == y:
    print("Yes")
if x == z:
    print("Yes")
if y == z:
    print("Yes")
