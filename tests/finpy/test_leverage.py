import pytest

from finpy.leverage import expected_loss, leverage_quotient, debt_ratio


@pytest.mark.parametrize(
    'prob_default, exposure_default, loss_default, expected', [
        (0.04, 725, 0.25, 21.75), ])
def test_expected_loss(prob_default, exposure_default, loss_default, expected):
    assert expected_loss(prob_default, exposure_default, loss_default) == expected


def test_leverage_quotient():
    assert leverage_quotient(50, 100) == 0.5


def test_debt_ratio():
    assert debt_ratio(50, 100) == 2/3
