from finpy.weighted_average_cost_of_capital import present_value, weighted_average_cost_of_capital
import pytest


@pytest.mark.parametrize(
    'series_of_payments, wacc, _present_value', [
        ([100, 80, 60, 150], 0.05, 343.03608),
        ([100, 80, 60, 150], 0.07, 326.7452),
    ]
)
def test_present_value(series_of_payments, wacc, _present_value):
    assert present_value(series_of_payments, wacc) == pytest.approx(_present_value, 0.001)


def test_weighted_average_cost_of_capital():
    assert weighted_average_cost_of_capital(0.1, 0.9, 0.1, 0.08, 0.3) == pytest.approx(0.0604, 0.001)