#Дано три числа.
#Найти количество положительных чисел среди них.

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

summ = 0

if x > 0:
    summ += 1
if y > 0:
    summ += 1
if z > 0:
    summ += 1

print(summ)
