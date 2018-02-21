#Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.

x = int(input("x:"))
y = int(input("y:"))

if x - 100 == y:
    print("Yes")
else:
    print("No")
