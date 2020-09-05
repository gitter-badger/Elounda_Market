#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def run(sql_answer, retail_price):
    # create your figure here
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='Product', ylabel='Retail Price', title='Retail Price [Scatter Plot]')
    plt.scatter(range(len(sql_answer)), retail_price, marker='o', color='blue', label='ELOUNDA')
    plt.scatter(range(len(sql_answer)), sql_answer['ΤΙΜΗ BAZAAR'], marker='o', color='red', label='BAZAAR')
    # plt.scatter(range(len(sql_answer)), sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'], marker='o', color='green',
    # label='ΒΑΣΙΛΟΠΟΥΛΟΣ') plt.scatter(range(len(sql_answer)), sql_answer['TIMH Care Market'], marker='o',
    # color='black', label='Care Market')
    plt.grid(True, alpha=0.2)
    plt.legend()
    plt.savefig('views.png')
    # plt.show()