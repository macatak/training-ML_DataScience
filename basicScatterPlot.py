#!/usr/bin/python3

'''
uses a CSV that maps production budgets vs worldwide gross
'''

import pandas
from pandas import DataFrame

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression



data = pandas.read_csv('/data/github/ML-DS-bootcamp/cost-revenue-clean.csv')

data.describe()

x = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])

# setup a scatter plot
# alpha sets the transparency
plt.scatter(x, y, alpha=0.3)
# formatting
plt.title('Film cost vs Global revenue')
plt.xlabel("Production Budget $")
plt.ylabel("Worldwide Gross $")
# set the upper and lowerlimits
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
# display it
plt.show()
