#Пользователь вводит количество недель, месяцев, лет и получает количество дней за это время.
# Считать, что в месяце 30 дней.

week = int(input("week:"))

month = int(input("month:"))

year = int(input("year:"))

day = week * 7 + month * 30 + year * 360

print(day)
