#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt
import squarify


def run(answer, answer_2):
    X = answer_2['YEAR']
    y = answer_2['TurnOver']
    plt.figure(figsize=(16, 8))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ', title='ELOUNDA MARKET (ΚΕΡΟΥΛΗΣ)')
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
    plt.savefig('images/keroulis_views.png')
    # plt.show()

    # -------------------- TREE MAP --------------------
    # Prepare Data
    df = answer[answer.TurnOver > 0]
    labels = df.apply(lambda x: f'{x[0]}\n({x[1]} EUR)', axis=1)
    print(labels)
    sizes = df['TurnOver'].values.tolist()
    colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]

    # Draw Plot
    plt.figure(figsize=(16, 8), dpi=300)
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.9)

    # Decorate
    plt.title(f'ΤΖΙΡΟΣ / ΥΠΟΚΑΤΗΓΟΡΙΑ')
    plt.axis('off')
    plt.savefig('images/keroulis_tree_map.png')
    # plt.show()
