#Робот может перемещаться в четырех направлениях
#(«11» — север, «12» — запад, «13» — юг, «14» — восток)
#  и принимать три цифровые команды: 0 — продолжать
# движение, 1 — поворот налево, –1 — поворот направо.
# Дан число (11, 12, 13 или 14) — исходное направление
# робота и целое число N (0, 1 или -1) — посланная ему
# команда. Вывести направление робота после выполнения
# полученной команды (то есть север, запад, юг или восток).

n = 11
w = 12
e = 13
s = 14

N = int(input("Input 0, 1 or -1 ,n="))

if N == 0:
    print(n+1,w,e,s)

if N == 1:
    print(n,w,e+1,s)

if N == -1:
    print(n,w,e,s+1)




