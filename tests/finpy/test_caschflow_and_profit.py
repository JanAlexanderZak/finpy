import pytest
from finpy.caschflow_and_profit import cashflow_and_profit


@pytest.mark.parametrize(
    'cash_profit, non_cash_profit, cash_expense, non_cash_expense, expected', [
        (100, 50, 80, 40, (20, 30)),
        (-100, 50, 80, 40, (-180, -170)),
    ], )
def test_cashflow_and_profit(cash_profit, non_cash_profit, cash_expense, non_cash_expense, expected):
    assert cashflow_and_profit(cash_profit, non_cash_profit, cash_expense, non_cash_expense) == expected
