#Дано четырехзначное число.
# Верно ли, что цифр в нем расположены по убыванию?
# Например, 4311 - нет, 4321 - да, 5542 - нет,
# 5631 - нет, 9871 - да.

value = int(input("Value:"))

digit_1 = value // 1000
digit_2 = value // 100 % 10
digit_3 = value // 10 % 10
digit_4 = value % 10


if digit_2 == digit_1-1 and digit_3 == digit_2-1 and digit_4 == digit_3-1:

    print("Yes")

else:
    print("No")



