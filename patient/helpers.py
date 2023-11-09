from dateutil.relativedelta import *



def calc_age(birth_date, date_to_compare):
    if birth_date and birth_date < date_to_compare:
        age = relativedelta(date_to_compare, birth_date)
        if age.years >= 10:
            age = {"lat": age.years}
        elif 10 > age.years >= 1:
            age = {"lat": age.years,
                   'miesięcy': age.months}
        else:
            age = {'miesięcy': age.months,
                   'dni': age.days}
        return age