#Дано трехзначное число.
# Переставьте первую и последнюю цифры.

value = int(input("value:"))

digit_1 = value // 100
digit_2 = value // 10 % 10
digit_3 = value % 10

buff = digit_1
buff1 = digit_3

digit_1 = buff1
digit_3 = buff

print(digit_1,digit_2,digit_3)
