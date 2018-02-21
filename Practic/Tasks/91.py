#Найти сумму 2/3+3/4+4/5+...+9/10.
from fractions import Fraction
i = Fraction(2, 3)
g = 0
while i <= Fraction(9, 10):
    i += Fraction(1, 1)
    g += i
    print(g)
