#Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c.
t = int(input("t:"))
s = int(input("s:"))

t = t / 60

s = s /1000

print("V:",s/t)
