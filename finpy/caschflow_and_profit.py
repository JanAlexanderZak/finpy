import pandas as pd
import plotly.express as px


def cashflow_and_profit(cash_profit, non_cash_profit, cash_expense, non_cash_expense):
    """ Calculate cashflow and profit
    :param cash_profit: cash
    :param non_cash_profit: eg. claims from suppliers
    :param cash_expense: cash
    :param non_cash_expense: eg. demands from suppliers
    :return: cashflow, profit
    """
    cashflow = cash_profit - cash_expense
    profit = cashflow + (non_cash_profit - non_cash_expense)
    return cashflow, profit


if __name__ == '__main__':
    df = pd.DataFrame(
        [['Company A', 'profit', 100, 50],
         ['Company A', 'expense', 80, 40], ],
        columns=['Company', 'Profit/Expense', 'Cash', 'Non_Cash'])

    # Visualize
    fig = px.bar(df, x='Profit/Expense', y=['Cash', 'Non_Cash'], title="Wide-Form Input")
    fig.update_layout(xaxis=dict(type='category'))
    fig.show()
