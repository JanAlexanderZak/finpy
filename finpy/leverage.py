""" Leverage Quotient and Debt Ratio
todo: define class
"""


def leverage_quotient(debt, equity):
    return debt / equity


def debt_ratio(debt, equity):
    return equity / (equity + debt)


def expected_loss(probability_default: float, exposure_default: float, loss_default: float):
    """
    :param probability_default: Probability of default for one year ( eg. 4% means every 25 years)
    :param exposure_default: Value of credit in given year
    :param loss_default: how much is lost if credit defaults ( eg. loss_default = 25% means 75% is lost
    :return: expected loss for given year
    """
    return probability_default * exposure_default * (1 - loss_default)


if __name__ == '__main__':
    print(leverage_quotient(200, 100))
    print(debt_ratio(200, 100))
