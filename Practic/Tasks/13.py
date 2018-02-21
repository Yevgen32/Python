#Вычислите значение выражения x2+b−−−−−√5−b2sin3(x+a)x при a=0.1, b=0.2 и x=1

import math

a = 0.1
b = 0.2
x = 1

print(math.pow(x**2 + b, 5) - (b**2*math.sin(x+a)**3) /x)
