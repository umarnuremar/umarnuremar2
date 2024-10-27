money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
# счетчик месяцев
months = 0

# бюджет сейчас
current_budget = money_capital + salary

# пока можно покрывать расходы
while current_budget >= spend:
    # счетчик месяцев
    months += 1

    # расходы с учетом роста цен (начиная со второго месяца)
    if months > 1:
        spend *= (1 + increase)

    # обновленный бюджет
    current_budget = current_budget - spend + salary


print("Количество месяцев, которое можно протянуть без долгов:", months)n