def present_value(_series_of_payments, wacc=0.05):
    _present_value = 0
    for i, val in enumerate(_series_of_payments):
        # print(f"{val} / ((1 + 0.05) ** {i + 1}) = ", val / ((1 + 0.05) ** (i + 1)))
        _present_value += val / ((1 + wacc) ** (i + 1))
    return round(_present_value, 5)


def weighted_average_cost_of_capital(equity, debt, equity_cost, interest, tax):
    # equity cost is the return on capital in free market
    # interest is the similar cost for debt
    wacc = (equity / (equity + debt) * equity_cost) + (debt / (debt + equity) * interest) * (1 - tax)
    return wacc


if __name__ == '__main__':
    print(present_value([100, 80, 60, 150], 0.07))
    print(weighted_average_cost_of_capital(0.1, 0.9, 0.1, 0.08, 0.3))
