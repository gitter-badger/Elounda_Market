#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import matplotlib.pyplot as plt


def run(df):
    X = df['USER']
    y = df['ΝΕΑ ΕΙΔΗ']
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΧΡΗΣΤΗΣ', ylabel='ΝΕΑ ΕΙΔΗ', title='ΝΕΑ ΕΙΔΗ / ΧΡΗΣΤΗ ΓΙΑ ΤΟ ΤΡΕΧΟΝ ΕΤΟΣ')
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
    plt.savefig('images/new_items_per_user.png')
    # plt.show()
    plt.close()
#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

