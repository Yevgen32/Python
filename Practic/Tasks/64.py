#Дано четырехзначное число. Если оно читается слева направо и справа налево одинаково, то вывести yes, иначе no.

value = int(input("Value:"))


digit_1 = value // 1000
digit_2 = value // 100 % 10
digit_3 = value // 10 % 10
digit_4 = value % 10

if digit_1 == digit_4 and digit_2 == digit_3:
    print("YES")
else:
    print("NO")
