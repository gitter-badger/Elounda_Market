#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def plot_greece_graph(df):
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ACTIVE DAYS', ylabel='DEATHS', title='Greece COVID DEATHS GRAPHS / TIME')
    plt.plot(range(len(df.total_deaths[df.total_deaths > 0])),
             df.total_deaths[df.total_deaths > 0], label='GREECE')
    plt.grid(True, alpha=0.2)
    plt.legend()
    # plt.show()
    plt.savefig('images/greece_deaths.png')
    plt.close()
