#Вычислите 1⋅2+2⋅3⋅4+...+n⋅(n+1)⋅…⋅2n.
# 2 + 24 + 72 = 98
i = 0
n = 4
sum = 1
buf = 0
while i < n:
    i += 1

    if i == 1:
        sum = i * (i + 1) * (i)
        buf += sum
    if i > 1:
        sum = i * (i + 1) * (i*2)
        buf += sum
print(buf)


