#Для данного n найти сумму 1+2+3+...+n. Например, для n=10 ответ равен 55.

n = int(input("n:"))

i = 0

g = 0

while i < n:
    i +=1
    g +=i
    print(g)
