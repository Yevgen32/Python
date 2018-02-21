#Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.

value = int(input("value:"))

digit_1 = value // 1000
digit_2 = value // 100 % 10
digit_3 = value // 10 % 10
digit_4 = value % 10

maxx = digit_1

minn = digit_1

if digit_1 < digit_2:
    maxx = digit_2
if maxx < digit_3:
    maxx = digit_3
if maxx < digit_4:
    maxx = digit_4
if digit_1 > digit_2:
    minn = digit_2
if minn > digit_3:
    minn = digit_3
if minn > digit_4:
    minn = digit_4

print(maxx,minn)

buff = minn
buff1 = 0
buff2 = 0

if maxx == digit_1:
    digit_1 = maxx
    buff1 = digit_1 #max
    digit_1 = minn
if maxx == digit_2:
    digit_2 = maxx
    buff1 = digit_2
    digit_2 = minn
if maxx == digit_3:
    digit_3 = maxx
    buff1 = digit_3
    digit_3 = minn
if maxx == digit_4:
    digit_4 = maxx
    buff1 = digit_4
    digit_4 = minn


if minn == digit_1:
    digit_1 = minn
    buff2 = digit_1 #max
    digit_1 = maxx
if maxx == digit_2:
    digit_2 = minn
    buff2 = digit_2
    digit_2 = maxx
if maxx == digit_3:
    digit_3 = minn
    buff2 = digit_3
    digit_3 = maxx
if maxx == digit_4:
    digit_4 = minn
    buff2 = digit_4
    digit_4 = maxx

print(digit_1,digit_2,digit_3,digit_4)
