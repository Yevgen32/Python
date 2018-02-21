#Даны три числа. Написать "yes", если можно взять какие-то два из них и в сумме получить третье


x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x + y == z:
    print("Yes")
if x + z == y:
    print("Yes")
if y + z == x:
    print("Yes")
