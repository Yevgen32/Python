#Вывести на экран:
#AAABBBAAABBBAAABBB
#BBBAAABBBAAABBBAAA
#AAABBBAAABBBAAABBB
#(таких строк n, в каждой строке m троек AAA)

n = int(input("n:"))
m = int(input("m:"))
i = 0
while i < n:
    i+=1
    print("AAABBB" * m)
    print("BBBAAA" * m)
