#Даны два числа. Если первое число больше второго, то вывести yes, иначе поменять значения этих переменных и вывести их на экран


x = int(input("x:"))
y = int(input("y:"))

if x > y:
    print("yes")
else:
    buff = x
    x = y
    y = buff
    print(x,y)
