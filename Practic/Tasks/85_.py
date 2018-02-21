#Пользователь вводит количество строк. Вывести на экран логотип соответствующего размера. Если текст не помещается, то вывести логотип без текста.

a = int(input("a:"))
b = int(input("b:"))

for i in range(a):
    if i == 0 or i == a:
        for j in range (a):
            print ("[", end= " ")

    else:
        print("[", end=" ")
        for j in range (1, b):
            print(":", end= " ")
        print("[", end= " ")
    print()
