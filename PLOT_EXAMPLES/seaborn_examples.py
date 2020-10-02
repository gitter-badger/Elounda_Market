#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('/csv/gradebook.csv')
df_survey = pd.read_csv('/csv/survey.csv')
print(df)

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")


# BY DEFAULT MEAN AND 95% CONFIDENCE
sns.barplot(data=df, x='name', y='grade')
plt.show()
# Αλλαγή από "bootstrapped confidence interval" σε "standar deviation" ci = 'sd'
sns.barplot(data=df, x='name', y='grade', ci='sd')
plt.show()
# MEDIAN
sns.barplot(data=df_survey, x='Gender', y='Response', estimator=np.median)
plt.show()
# LEN
plt.subplot(title='Multiple Columns hue')
sns.barplot(data=df_survey, x='Gender', y='Response', estimator=len)
plt.show()
# Multiple Columns hue
plt.subplot(title='Multiple Columns hue')
sns.barplot(data=df_survey, x='Age Range', y='Response', hue='Gender')
plt.show()


# KDE PLOTS