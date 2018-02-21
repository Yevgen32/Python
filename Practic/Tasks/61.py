#Дано четырехзначное число. Определите, есть ли одинаковые цифры в нем.


value = int(input("Value:"))


digit_1 = value // 1000
digit_2 = value // 100 % 10
digit_3 = value // 10 % 10
digit_4 = value % 10

if digit_1 == digit_2 or digit_1 == digit_3 or digit_1 == digit_4 or digit_2 == digit_3 or digit_2 == digit_4 or digit_3 == digit_4:
    print("Yes")
else:
    print("no")
