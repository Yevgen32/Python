#Пользователь вводит три числа. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x > 10 and y > 10 and z > 10 and x % 3 == 0 and y % 3 == 0:
    print("yes")
else:
    print("No")
