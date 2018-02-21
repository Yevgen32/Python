#Вычислите значение выражения |x−5|−sinx3+x2+2014−−−−−−−−√cos2x−3 при x=−2.34. Ответ: -1.76911
import math

x = -2.34

print( ( (math.fabs(x-5) - math.sin(x))/3 ) + ( math.sqrt(x**2 + 2014)) * math.cos(2 * x) - 3 )

