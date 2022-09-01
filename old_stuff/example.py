main_debt = 31200
main_debt_first = main_debt
fee = 10
days = int(input("Сколько дней просрочки? "))


def r(d):
    return round(d, 2)



for i in range(days):
    fee_oncome = main_debt * fee / 36500
    main_debt += fee_oncome
    print(f"Дневные проценты за {i + 1} день: {r(fee_oncome)}. Общая сумма долга: {r(main_debt)}")

print("\n")
print(f"Общий долг на сегодня: {r(main_debt)}")
print(f"Сумма накопленных процентов при расчете каждый день: {r(main_debt - main_debt_first)}")
# print(f"Сумма накопленных процентов при расчете раз в год: {r(main_debt_first*fee/100)}")
# print(f"Разница расчетах: {r(main_debt - main_debt_first-(main_debt_first*fee/100))}")