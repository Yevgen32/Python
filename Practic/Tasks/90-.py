#Найти сумму cos3/5+cos5/7+cos7/9+...+cos111/113.

import math
from fractions import Fraction

i = math.cos(Fraction(3, 5))
g = 0

while i > math.cos(Fraction(111, 113)):
    i += math.cos(Fraction(4, 35))
    g =+ i
    print(g)
