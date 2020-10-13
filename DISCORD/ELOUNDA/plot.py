#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt
import seaborn as sns


def elounda_market_sales(df, df_pivot):
    X = df.YEAR.unique()
    y = df_pivot['ΣΥΝΟΛΑ']
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ', title='ELOUNDA MARKET')
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
    plt.savefig('images/views.png')
    # plt.show()
    plt.close()


def kataskevastes(ccplot, name):
    X = ccplot.YEAR
    y = ccplot.TurnOver
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='ΤΖΙΡΟΣ', title=name)
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
    plt.savefig('images/kataskevastis_views.png')
    plt.close()


def heatmap(df):
    f, ax = plt.subplots(figsize=(15, 9))
    cmap = sns.diverging_palette(133, 10, as_cmap=True)
    sns.heatmap(df, annot=True, fmt='.2f', linewidths=.5, ax=ax, cmap=cmap).set(title='ELOUNDA MARKET')
    plt.savefig('images/heatmap.png')
    # plt.show()
    plt.close()


def box(df):
    fig = plt.subplots(figsize=(15, 9))
    sns.boxplot(data=df, x='YEAR', y='TurnOver', palette="light:#5A9")
    plt.savefig('images/box.png')
    # plt.show()
    plt.close()


def heatmap_blue(df, name):
    f, ax = plt.subplots(figsize=(15, 9))
    cmap="YlGnBu"
    sns.heatmap(df, annot=True, fmt='.2f', linewidths=.5, ax=ax, cmap=cmap).set(title=f'{name}')
    plt.savefig('images/heatmap.png')
    # plt.show()
    plt.close()
