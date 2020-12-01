import pandas as pd
import plotly.express as px
import numpy as np


def debt_capacity(profit: pd.Series, depreciation: pd.Series, running_cost: pd.Series, debt: pd.Series):
    """
    :param profit:
    :param depreciation:
    :param running_cost:
    :param debt:
    :return:
    """
    return 7 * free_cashflow(profit, depreciation, running_cost) - np.average(debt)


def free_cashflow(profit: pd.Series, depreciation: pd.Series, running_cost: pd.Series):
    """
    :param profit:
    :param depreciation:
    :param running_cost:
    :return:
    """
    return average_cashflow(profit, depreciation) - np.average(running_cost)


def average_cashflow(profit: pd.Series, depreciation: pd.Series):
    """
    :param profit:
    :param depreciation:
    :return:
    """
    return np.average(profit + depreciation)


if __name__ == '__main__':
    df = pd.DataFrame(
        [['Company A', '2000', 50, 10, 30, 10],
         ['Company A', '2001', 55, 20, 29, 20],
         ['Company A', '2002', 65, 20, 31, 20], ],
        columns=['Company', 'Year', 'Profit', 'Depreciation', 'Running Cost', 'Debt'])

    # Visualize
    fig = px.bar(df, x='Year', y=['Profit', 'Depreciation'], title="Wide-Form Input")
    fig.update_layout(xaxis=dict(type='category'))
    fig.show()

    print(debt_capacity(df['Profit'], df['Depreciation'], df['Running Cost'], df['Debt']))
    print(free_cashflow(df['Profit'], df['Depreciation'], df['Running Cost']))
    print(average_cashflow(df['Profit'], df['Depreciation']))

