import pytest

from finpy.gordon_growth_model import growth_rate, predict_price, gordon_growth_model, implicit_growth_rate, company_valuation


def test_growth_rate():
    assert growth_rate(23, 5.6, 16) == pytest.approx(0.08450, 4)


def test_predict_price():
    assert predict_price(23, 0.092, 1) == pytest.approx(27.4266, 3)


def test_gordon_growth_model():
    assert gordon_growth_model(10, 0.09, 0.04) == pytest.approx(200)


def test_implicit_growth_rate():
    assert implicit_growth_rate(0.5, 10, 100) == 0.05


def test_company_valuation():
    assert company_valuation(300000, 0.1, 0.08) == pytest.approx(14999999.99, 2)
