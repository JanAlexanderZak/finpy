import pytest

from finpy.dividends import Dividends


class TestDividends:
    def test_dividend_yield(self):
        dividends = Dividends()
        assert dividends.dividend_yield(0.06, 100, 0.07, 4) == pytest.approx(
            [5.607, 5.240, 4.897, 4.577, 76.289], 3)
