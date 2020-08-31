#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from matplotlib.pyplot import figure
import mpld3

fig = figure()
ax = fig.gca()
ax.plot([1,2,3,4])

mpld3.show(fig)
