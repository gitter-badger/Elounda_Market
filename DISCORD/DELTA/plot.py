#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import matplotlib.pyplot as plt


def run(answer_2):
    X = answer_2['YEAR']
    y = answer_2['TurnOver']
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ', title='ELOUNDA MARKET (ΦΡΕΣΚΟ ΓΑΛΑ ΔΕΛΤΑ)')
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.bar(X, y, alpha=0.9, color=colors)
    for a, b in zip(X, y):
        label = "{:.2f} €".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)
    plt.savefig('images/fresco_gala_delta_views.png')
    # plt.show()
