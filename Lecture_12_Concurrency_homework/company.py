from datetime import datetime, timedelta


class Company:
    __slots__ = ["name", "price", "code", "p_e", "year_growth", "income"]

    def __init__(self, name, price, code, p_e, year_growth, income):
        self.name = name
        self.price = price
        self.code = code
        self.p_e = p_e
        self.year_growth = year_growth
        self.income = income
