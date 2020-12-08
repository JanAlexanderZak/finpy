"""
Formula:
present_value = future_payment / ((1 + interest) ** year)
"""
import numpy as np


class Discounting:
    def __init__(self):
        pass

    @staticmethod
    def future_payment(_interest, _present_value, _year):
        return _present_value * ((1 + _interest) ** _year)

    @staticmethod
    def interest(_future_payment,_present_value, _year):
        return (_future_payment / _present_value) ** (1 / _year) - 1

    @staticmethod
    def present_value(_future_payment, _interest, _year):
        return _future_payment / ((1 + _interest) ** _year)

    @staticmethod
    def year(_future_payment, _interest, _present_value):
        return np.log(_future_payment / _present_value) / np.log(1 + _interest)


if __name__ == '__main__':
    discount = Discounting()
    present_value = discount.present_value(100, 0.0526, 1)
    interest = discount.interest(100, 50, 10)
    year = discount.year(100, 0.0717, 50)
    payment = discount.future_payment(0.0717, 50, 10)
    print(present_value)
    print(interest)
    print(year)
    print(payment)
