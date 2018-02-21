#Вычислите значение выражения ex−2+|sin(x)|−x10⋅cos1x при x=3.6
import math
x = 3.6
print( (math.exp(x-2)) + (math.fabs(math.sin(x))) - (x**10 * math.cos(1/x)) )
