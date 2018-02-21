#Вывести на экран числа от 1000 до 9999 такие, что среди цифр нет цифр 5 и цифры 6.

value = 999
while value < 9999:
    value += 1
    digit_1 = value // 1000
    digit_2 = value // 100 % 10
    digit_3 = value // 10 % 10
    digit_4 = value % 10
    if digit_1 != 5 and digit_1 != 6 and digit_2 != 5 and digit_2 != 6 and digit_3 != 5 and digit_3 != 6 \
            and digit_4 != 5 and digit_4 != 6:
        print(value)
