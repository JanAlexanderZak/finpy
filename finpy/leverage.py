""" Leverage Quotient and Debt Ratio
"""


def leverage_quotient(debt, equity):
    return debt / equity


def debt_ratio(debt, equity):
    return equity / (equity + debt)


if __name__ == '__main__':
    print(leverage_quotient(200, 100))
    print(debt_ratio(200, 100))
