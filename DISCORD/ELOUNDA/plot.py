#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def run_01(prod_per_year):
    X = prod_per_year['YEAR']
    y = prod_per_year['TurnOver']
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


def run_02(year_2012, year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, kataskevastes_lst, c):
    plt.figure(figsize=(50, 50))
    j = 1
    for i in range(len(c)):
        percent = int((100 * (i + 1)) / len(c))
        filler = "█" * percent
        remaining = '-' * (100 - percent)
        y = []
        y.append(year_2012[i])
        y.append(year_2013[i])
        y.append(year_2014[i])
        y.append(year_2015[i])
        y.append(year_2016[i])
        y.append(year_2017[i])
        y.append(year_2018[i])
        y.append(year_2019[i])
        y.append(year_2020[i])
        X = ['12', '13', '14', '15', '16', '17', '18', '19', '20']
        Y = y
        plt.subplot(8, 8, j, ylabel='ΤΖΙΡΟΣ', title=kataskevastes_lst[i])
        colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
        plt.bar(X, y, color=colors)
        j += 1
        print(f'\r 20: EXCEL looping with counter {i} Done:[{filler}{percent}%{remaining}]', end='', flush=True)

    plt.grid(True, alpha=0.5)
    plt.savefig('images/kataskevastis_views.png')
    # plt.show()
    print('\n 21: PLOT DONE')
    plt.close()