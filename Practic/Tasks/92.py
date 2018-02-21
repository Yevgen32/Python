#Вывести на экран сто первых сумм вида 1+2+3+...+n.
i = 0
n = int(input("n:"))
summ = 0
while i < n:
    i+=1
    summ+=i
print(summ)
