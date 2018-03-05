#Вывести на экран:
#AAAAAAAAAAAAAAAA
#ABBBBBBBBBBBBBBA
#ABBBBBBBBBBBBBBA
#ABBBBBBBBBBBBBBA
#AAAAAAAAAAAAAAAA
#(количество строк вводит пользователь, ширина прямоугольника в два раза больше высоты)

a = int(input("a:")) # высота
b = a * 2 # ширина
n = 0

for i in range(b):
    print("A", end="")
for j in range(a):
    print("A")
