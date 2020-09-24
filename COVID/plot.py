#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def plot_greece_graph(gr, it):
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ACTIVE DAYS', ylabel='DEATHS', title='Greece COVID DEATHS GRAPHS / TIME')
    plt.plot(range(len(gr.total_deaths[gr.total_deaths > 0])),
             gr.total_deaths[gr.total_deaths > 0], label=f'{gr.location.unique()}')
    # plt.plot(range(len(it.total_deaths[it.total_deaths > 0])),
    #          it.total_deaths[it.total_deaths > 0], label=f'{it.location.unique()}')

    plt.grid(True, alpha=0.2)
    plt.legend()
    # plt.show()
    plt.savefig('images/greece_deaths.png')
    plt.close()
