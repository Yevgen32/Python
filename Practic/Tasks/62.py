#Дано пятизначное число. Цифры на четных позициях занулить. Например, из 12345 получается число 10305.


value = int(input("Value:"))


digit_1 = value // 10000
digit_2 = value // 1000 % 10
digit_3 = value // 100 % 10
digit_4 = value // 10 % 10
digit_5 = value % 10

if digit_1 % 2 == 0:
    digit_1 = 0
if digit_2 % 2 == 0:
    digit_2 = 0
if digit_3 % 2 == 0:
    digit_3 = 0
if digit_4 % 2 == 0:
    digit_4 = 0
if digit_5 % 2 == 0:
    digit_5 = 0
print(digit_1,digit_2,digit_3,digit_4,digit_5)
