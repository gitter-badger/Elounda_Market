#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

# t = 2 # There are two sets of data: A and B
# w = 0.8 # We generally want bars to be 0.8
# n = 1 # A is first set of data
# d = 5 # There are 5 topics we're plotting (len of list)


# Make your chart here
plt.figure(figsize=(10,8))
school_a_x = create_x(2, .8, 1, 5)
school_b_x = create_x(2, .8, 2, 5)
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax = plt.subplot(title='Test Averages on Different Units', xlabel='Unit', ylabel='Test Average')
plt.bar(school_a_x, middle_school_a, label='Middle School A')
plt.bar(school_b_x, middle_school_b, label='Middle School B')
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend()
plt.savefig('images/my_side_by_side.png')
plt.show()
