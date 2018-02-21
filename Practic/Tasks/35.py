#Дано число. Если оно меньше 7, то вывести Yes, если больше 10, то вывести No, если равно 9, то вывести Error.

x = int(input("x:"))
if x < 7:
    print("Yes")
elif x > 10:
    print("No")
elif x == 9:
    print("Error")
