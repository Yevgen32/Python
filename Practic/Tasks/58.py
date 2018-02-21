#Дано две даты, каждая из которых состоит из трех чисел
#  (день, месяц и год). Вывести yes,
# если первая дата раньше второй, иначе вывести no.

d = int(input("d:"))
m = int(input("m:"))
y = int(input("y:"))

d1 = int(input("d1:"))
m1 = int(input("m1:"))
y1 = int(input("y1:"))

if y > y1:
    print(d,m,y)
elif m > m1:
    print(d,m,y)
elif d > d1:
    print(d,m,y)

else:
    print(d1,m1,y1)
