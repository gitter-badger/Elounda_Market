#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import matplotlib.pyplot as plt
import seaborn as sns

def run(df, df2):
    X = df['YEAR']
    y = df['ΚΑΤΑΜΕΤΡΗΣΗ']
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΚΑΤΑΜΕΤΡΗΣΗ', title='ΣΦΑΛΜΑΤΑ ΣΤΟ ΤΑΜΕΙΟ ΑΝΑ ΕΤΟΣ')
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.bar(X, y, alpha=0.9, color=colors)
    for a, b in zip(X, y):
        label = "{}".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)
    plt.savefig('images/no_item_found.png')
    # plt.show()
    plt.close()

    plt.figure(figsize=(15, 9))
    g4 = sns.FacetGrid(df2, col="STORE", col_wrap=3, height=4)
    g4 = (g4.map(plt.bar, "DATE", "COUNT").add_legend())
    plt.savefig('images/detailed.png')
    plt.close()
