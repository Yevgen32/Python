n, m, a = map(int, input().split(' '))
i = 0
s2 = 0
while n * m != s2:
    s2 += a + a
    if n * m <= s2:
        break
    i += 1
print(i)


