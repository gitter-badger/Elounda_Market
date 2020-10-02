#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import matplotlib.pyplot as plt
import seaborn as sns
from Private import sql_connect
import pandas as pd
from PLOT_EXAMPLES import sql
from datetime import datetime as dt

current_year = dt.now().year + 1
past_years = current_year - 5

df=pd.read_sql_query(sql.query_01(), sql_connect.connect())

# Setting styles: darkgrid, whitegrid, dark, white,
sns.set_style("dark")
sns.set_palette("pastel")

for i in range(past_years, current_year):
    year = df[df.YEAR == f'{i}'].TurnOver
    print(year)
    sns.kdeplot(year, shade=True, label=f'{i}')
plt.legend()
plt.show()

sns.barplot(data=df[df.YEAR >= str(past_years)], x='MONTH', y='TurnOver', hue='YEAR')
plt.show()

sns.boxplot(data=df[df.YEAR >= str(past_years)], x='YEAR', y='TurnOver')
plt.show()

sns.violinplot(data=df[df.YEAR >= str(past_years)], x="YEAR", y="TurnOver")
sns.despine(left=True, bottom=True)
plt.show()
