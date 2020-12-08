import pytest
from finpy.discounting import Discounting


class TestDiscounting:
    def test_future_payment(self):
        discount = Discounting()
        assert discount.future_payment(0.0717, 50, 10) == pytest.approx(99.931, 3)

    def test_interest(self):
        discount = Discounting()
        assert discount.interest(100, 50, 10) == pytest.approx(0.0717, 3)

    def test_present_value(self):
        discount = Discounting()
        assert discount.present_value(100, 0.0526, 1) == pytest.approx(95.002, 3)

    def test_year(self):
        discount = Discounting()
        assert discount.year(100, 0.0717, 50) == pytest.approx(10.009, 3)

    @pytest.mark.parametrize(
        'series_of_payments, wacc, _present_value', [
            ([100, 80, 60, 150], 0.05, 343.03608),
            ([100, 80, 60, 150], 0.07, 326.7452),
        ]
    )
    def test_present_value_wacc(self, series_of_payments, wacc, _present_value):
        discount = Discounting()
        assert discount.present_value_wacc(series_of_payments, wacc) == pytest.approx(_present_value, 0.001)

    def test_wacc(self):
        discount = Discounting()
        assert discount.wacc(0.1, 0.9, 0.1, 0.08, 0.3) == pytest.approx(0.0604, 0.001)
