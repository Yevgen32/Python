#Даны два трехзначных числа.
# Получите новое число присоединением
#  второго числа справа к первому без последних
# цифр у каждого. Например, 123 и 456 Ответ: 1245


value = int(input("Value:"))
value1 = int(input("Value:"))

digit_1 = value // 100
digit_2 = value // 10 % 10
digit_3 = value % 10

digit1 = value1 // 100
digit2 = value1 // 10 % 10
digit3 = value1 % 10

print(digit_1,digit_2,digit1,digit2)
