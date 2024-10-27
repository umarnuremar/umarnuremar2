salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
months = 10 # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# все траты
tot_expenses = 0

for month in range(months):
    tot_expenses += spend
    spend *= (1 + increase)  # увеличиваем расходы на 3%

# зп общая
tot_salary = salary * months

# подушка безопасности
money_capital = tot_expenses - tot_salary

# если подушка безопасности отрицательная то это означает что зп достаточно
if money_capital < 0:
    money_capital = 0

money_capital = round(money_capital)

print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital)