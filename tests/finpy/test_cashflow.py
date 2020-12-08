import pandas as pd
import pytest
from finpy.cashflow import Cashflow


class TestCashflow:
    @pytest.fixture
    def company_debt_history_df(self):
        # https://datatest.readthedocs.io/en/stable/how-to/fixtures/dataframe-fixture.html
        df = pd.DataFrame(
            [['Company A', '2000', 50, 10, 30, 10],
             ['Company A', '2001', 55, 20, 29, 20],
             ['Company A', '2002', 65, 20, 31, 20], ],
            columns=['Company', 'Year', 'Profit', 'Depreciation', 'Running Cost', 'Debt'], )
        cf = Cashflow(df['Profit'], df['Depreciation'], df['Running Cost'], df['Debt'])
        return df, cf

    @pytest.mark.parametrize(
        'cash_profit, non_cash_profit, cash_expense, non_cash_expense, expected', [
            (100, 50, 80, 40, (20, 30)),
            (-100, 50, 80, 40, (-180, -170)),
        ], )
    def test_cashflow_and_profit(self, cash_profit, non_cash_profit, cash_expense, non_cash_expense, expected, company_debt_history_df):
        _, cf = company_debt_history_df
        assert cf.cashflow_and_profit(cash_profit, non_cash_profit, cash_expense, non_cash_expense) == expected

    def test_debt_capacity(self, company_debt_history_df):
        df, cf = company_debt_history_df
        assert cf.debt_capacity() == pytest.approx(286.6666, 3)

    def test_free_cashflow(self, company_debt_history_df):
        df, cf = company_debt_history_df
        assert cf.free_cashflow() == pytest.approx(43.3333, 3)

    def test_average_cashflow(self, company_debt_history_df):
        df, cf = company_debt_history_df
        assert cf.average_cashflow() == pytest.approx(73.3333, 3)
