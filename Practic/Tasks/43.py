#Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)

x = int(input("x:"))

if x == 12 or x == 1 or x ==2:
    print("winter")
elif x == 3 or x == 4 or x == 5:
    print("spring")
elif x == 6 or x == 7 or x == 8:
    print("summer")
elif x == 9 or x == 10 or x == 11:
    print("autumn")
else:
    print("error")
