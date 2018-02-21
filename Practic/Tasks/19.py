#Пользователь вводит цены 1 кг конфет и 1 кг печенья.
# Найдите стоимость: а) одной покупки из 300 г конфет и 400 г печенья;
# б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.

sandy = int(input("sandy:"))
cookies = int(input("cookies:"))

first_buy = sandy * 0.3 + cookies * 0.4
second_buy = (2 * sandy + cookies) * 3

print(first_buy,'\t',second_buy)
