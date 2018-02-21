#Дано два числа. Если хотя бы одно из них больше 30, то вывести yes, иначе no.

x = int(input("x:"))
y = int(input("y:"))

if x > 30 or y > 30:
    print("Yes")
else:
    print("No")
