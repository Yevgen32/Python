#Дано четыре числа, если первые два числа больше 5, третье число делится на 6, четвертое число не делится на 3, то вывести yes, иначе no.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
v = int(input("v:"))

if x > 5 and y > 5 and z % 6 == 0 and v % 3 != 0:
    print("yes")
else:
    print("no")
