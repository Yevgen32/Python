#Дано три числа. Если ровно два из них  меньше 5, то вывести yes, иначе вывести no.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x and y < 5 or x and z < 5 or y and z < 5:
    print("Yes")

else:
    print("No")
