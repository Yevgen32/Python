4#Дано четырехзначное число. Переставьте местами цифры так, чтобы сначала оказались цифры, меньшие пяти.

value = int(input("Value:"))


digit_1 = value // 1000
digit_2 = value // 100 % 10
digit_3 = value // 10 % 10
digit_4 = value % 10


if digit_1 < 5:
    if digit_2 < 5:
        if digit_3 < 5:
            if digit_4 < 5:
                if digit_2 > digit_1 and digit_4 > digit_3:
                    print(digit_1,digit_2,digit_3,digit_4)
                elif digit_2 > digit_1 and digit_3 > digit_4:
                    print(digit_1,digit_2,digit_4,digit_3)
                elif digit_1 > digit_2 and digit_4 > digit_3:
                    print(digit_2,digit_1,digit_3,digit_4)
                elif digit_1 > digit_2 and digit_3 > digit_4:
                    print(digit_2,digit_1,digit_4,digit_3)
