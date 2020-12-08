"""

"""


def implicit_growth_rate(_return, _dividend, _stock_value):
    return _return * (_dividend / _stock_value)


def company_valuation(expected_profit, discount_rate, growth_rate):
    """
    :param expected_profit:
    :param discount_rate:
    :param growth_rate: can be organic or historic
    :return:
    """
    return expected_profit / (discount_rate - growth_rate)


if __name__ == '__main__':
    print(implicit_growth_rate(0.5, 10, 100))
    print(company_valuation(300000, 0.1, 0.08))  # 0.08 historic vs 0.04 organic
