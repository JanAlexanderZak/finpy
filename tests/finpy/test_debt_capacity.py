import pandas as pd
import pytest
from finpy.debt_capacity import debt_capacity, free_cashflow, average_cashflow


@pytest.fixture
def company_debt_history_df():
    # https://datatest.readthedocs.io/en/stable/how-to/fixtures/dataframe-fixture.html
    return pd.DataFrame(
        [['Company A', '2000', 50, 10, 30, 10],
         ['Company A', '2001', 55, 20, 29, 20],
         ['Company A', '2002', 65, 20, 31, 20], ],
        columns=['Company', 'Year', 'Profit', 'Depreciation', 'Running Cost', 'Debt'], )


def test_debt_capacity(company_debt_history_df):
    df = company_debt_history_df
    assert debt_capacity(df['Profit'], df['Depreciation'], df['Running Cost'], df['Debt']) == pytest.approx(286.6666, 3)


def test_free_cashflow(company_debt_history_df):
    df = company_debt_history_df
    assert free_cashflow(df['Profit'], df['Depreciation'], df['Running Cost']) == pytest.approx(43.3333, 3)


def test_average_cashflow(company_debt_history_df):
    df = company_debt_history_df
    assert average_cashflow(df['Profit'], df['Depreciation']) == pytest.approx(73.3333, 3)
