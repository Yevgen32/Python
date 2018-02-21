#Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5. Если таких чисел нет, то вывести error.


x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
summ = 0

if x % 5 == 0:
    summ += x
if y % 5 == 0:
    summ += y
if z % 5 == 0:
    summ += z

if summ == 0:
    print("error")
else:
    print(summ)


