#Найдите сумму 1+1/2+1/3+…+1/n.
from fractions import Fraction
n = int(input("n:"))
summ = 0
i = 1

while i <= n:
    summ += Fraction(1, i)
    i+=1
print(summ)
