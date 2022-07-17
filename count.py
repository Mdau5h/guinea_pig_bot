from datetime import datetime


def r(d):
    return round(d, 2)


def get_data():
    payday = datetime(2022, 7, 10)
    now_date = datetime.now()

    main_debt = 31200
    main_debt_first = main_debt
    fee = 10
    days = (now_date - payday).days

    for i in range(days):
        fee_oncome = main_debt * fee / 36500
        main_debt += fee_oncome

    data = {
        "days": days,
        "main_debt": r(main_debt),
        "every_day_fee": r(main_debt - main_debt_first),
    }
    return data




