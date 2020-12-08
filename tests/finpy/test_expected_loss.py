import pytest

from finpy.expected_loss import expected_loss


@pytest.mark.parametrize(
    'prob_default, exposure_default, loss_default, expected', [
        (0.04, 725, 0.25, 21.75), ])
def test_expected_loss(prob_default, exposure_default, loss_default, expected):
    assert expected_loss(prob_default, exposure_default, loss_default) == expected
