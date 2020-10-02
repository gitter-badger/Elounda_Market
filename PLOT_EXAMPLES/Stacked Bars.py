#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved


from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

plt.figure(figsize=(10,8))
ax = plt.subplot(title='Grade Distribution', xlabel='Unit', ylabel='Number of Students')
plt.bar(range(len(unit_topics)), As)
plt.bar(range(len(unit_topics)), Bs, bottom= As)
plt.bar(range(len(unit_topics)), Cs, bottom= c_bottom)
plt.bar(range(len(unit_topics)), Ds, bottom= d_bottom)
plt.bar(range(len(unit_topics)), Fs, bottom= f_bottom)
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.savefig('images/my_stacked_bar.png')
plt.show()