#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import matplotlib.pyplot as plt
import squarify


def app(answer_03, answer_04, answer_05):
    # ---------------- PLOT ----------------
    X = answer_05['YEAR']
    y = answer_05['Count "Παραστατικά"']
    plt.figure(figsize=(15, 9))
    plt.subplot(2, 1, 1, xlabel='ΕΤΟΣ', ylabel='Παραστατικά', title='(PDA STATISTICS) ΧΡΟΝΙΕΣ ')
    plt.bar(X, y, alpha=0.8)
    for a, b in zip(X, y):
        label = "{:.2f}".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)

    plt.subplot(2, 2, 3, xlabel='ΜΗΝΑΣ', ylabel='Παραστατικά', title='(PDA STATISTICS) ΜΗΝΕΣ')
    X = answer_04['MONTH']
    y = answer_04['Count "Παραστατικά"']
    plt.bar(X, y, alpha=0.8, color='red')
    for a, b in zip(X, y):
        label = "{:.2f}".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)

    plt.subplot(2, 2, 4, xlabel='ΗΜΕΡΑ', ylabel='Παραστατικά', title='(PDA STATISTICS) ΗΜΕΡΕΣ')
    X = answer_03['DAY']
    y = answer_03['Count "Παραστατικά"']
    plt.bar(X, y, alpha=0.8, color='yellow')
    for a, b in zip(X, y):
        label = "{:.2f}".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.5)
    plt.savefig('images/pda_views.png')
    # plt.show()

    # -------------------- TREE MAP --------------------
    # Prepare Data
    df = answer_05
    labels = df.apply(lambda x: f'{x[0]}\n({x[1]} Γραμμές)', axis=1)
    # print(labels)
    sizes = df['Count "Γραμμές"'].values.tolist()
    colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]

    # Draw Plot
    plt.figure(figsize=(16, 8), dpi=300)
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.9)

    # Decorate
    plt.title(f'ΓΡΑΜΜΕΣ / ΕΤΟΣ')
    plt.axis('off')
    plt.savefig('images/pda_tree_map.png')
    # plt.show()
    plt.close()
