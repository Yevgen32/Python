#Пользователь вводит сумму вклада в банк и годовой процент.
#Найдите сумму вклада через 5 лет
#(рассмотреть два способа начисления процентов)

sum = int(input('money:'))

proz = float(input('proz:'))

year = 5;

sum_proz = proz / 100 * sum

total = sum_proz * year + sum


print(total)
