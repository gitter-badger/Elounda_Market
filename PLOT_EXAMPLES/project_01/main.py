#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']


sns.set_style('whitegrid')
sns.set_context('poster', font_scale=.8)
f, ax = plt.subplots(figsize=(25, 10))
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title
plt.show()

df_goals = pd.read_csv('goals.csv')
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1.25)
sns.set_palette("Spectral")
f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals')
ax2.set_title('Goal Distribution / Year')
plt.show()
