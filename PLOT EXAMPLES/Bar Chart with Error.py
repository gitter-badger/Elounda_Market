#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from matplotlib import pyplot as plt
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
ax = plt.subplot(title='Final Exam Averages', xlabel='Year', ylabel='Test average')
plt.bar(years, past_years_averages, capsize=5, yerr=error)

# ax.set_xticks(range(len(years)))
# ax.set_xticklabels(years)
# plt.axis([-.5, 6.5, 70, 95])
plt.savefig('images/my_bar_chart.png')
plt.show()
plt.close()
