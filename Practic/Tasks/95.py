#Даны a и n. Вычислите p=(a+1)**2*(a+2)**2⋅…⋅(a+n)**2


#9 * 16 * 25 * 36 = 129600

a = 2
n = 4
i = 0
res = 1
while i < n:
    i += 1
    p = (a + i) ** 2
    res = res * p
print(res )

