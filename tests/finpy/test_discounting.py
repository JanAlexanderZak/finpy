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
