from dateutil.relativedelta import *
from datetime import date


def calc_age(birth_date):
    if birth_date and birth_date < date.today():
        age = relativedelta(date.today(), birth_date)
        if age.years > 10:
            age = {"lat": age.years}
        elif 10 > age.years > 1:
            age = {"lat": age.years,
                   'miesięcy': age.months}
        else:
            age = {'miesięcy': age.months,
                   'dni': age.days}
        return age