#Вывести на экран числа от 1000 до 9999 такие, что все цифры различны.

for value in range(1000, 9999):
    digit_1 = value // 1000
    digit_2 = value // 100 % 10
    digit_3 = value // 10 % 10
    digit_4 = value % 10
    if digit_1 != digit_2 and digit_1 != digit_3 and digit_1 != digit_4 and digit_2 != digit_3 and digit_2 != digit_4 and digit_3 != digit_4:
        print(value)

