#Пользователь вводит четыре числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
v = int(input("v:"))

maxx = -10000
if x % 2 == 0:
    if x > maxx:
        maxx = x
if y % 2 == 0:
    if y > maxx:
        maxx = y
if z % 2 == 0:
    if z > maxx:
        maxx = z
if v % 2 == 0:
    if v > maxx:
        maxx = v
if maxx == -10000:
    print("not found")


print(b)
