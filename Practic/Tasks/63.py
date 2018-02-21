#Даны два трехзначных числа. Найдите шестизначное число, образованное из двух данных чисел путем дописывания второго числа к первому справа.

value = int(input("Value:"))
value1 = int(input("Value:"))

digit_1 = value // 100
digit_2 = value // 10 % 10
digit_3 = value % 10

digit1 = value1 // 100
digit2 = value1 // 10 % 10
digit3 = value1 % 10

print(digit_1,digit_2,digit_3,digit1,digit2,digit3)
