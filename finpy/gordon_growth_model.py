"""
Cant predict value of all individual dividends in the future
Expected growth is:
Dn = D1 * (1 + g) ^ (n - 1)   ; g = growth rate of dividend, r = diskont rate ( diminishing returns in future )
"""


def growth_rate(past_value, present_value, time_delta):
    """ Growth rate of a dividend
    :param past_value: past value
    :param present_value: present value
    :param time_delta: years between x1 and x2
    :return: growth rate
    """
    return 1 - ((present_value / past_value) ** (1 / time_delta))


def predict_price(present_value, growth_rate, num_years):
    return present_value * (1 + growth_rate) ** (num_years + 1)


def gordon_growth_model(dividend, discount_rate, growth_rate):
    present_value = dividend / (discount_rate - growth_rate)
    return present_value


# income of 9600 per year, growth of 0.015, discount of 0.04
dividend = 10
gordon_growth_model(dividend, 0.09, 0.04)

print(growth_rate(23, 5.6, 16))
print(predict_price(23, 0.092, 1))
