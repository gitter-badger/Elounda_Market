#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def run(sql_answer, retail_price):
    # create your figure here
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='Product', ylabel='Retail Price', title='Retail Price [Scatter Plot]')
    plt.bar(range(len(sql_answer)), retail_price, label='ELOUNDA', alpha=.4)
    plt.scatter(range(len(sql_answer)), sql_answer['ΤΙΜΗ BAZAAR'], marker='o', label='BAZAAR', alpha=.4)
    plt.plot(range(len(sql_answer)), sql_answer['ΚΑΘΑΡΗ ΤΙΜΗ'], label='ΚΑΘΑΡΗ ΤΙΜΗ', alpha=.4)
    # plt.scatter(range(len(sql_answer)), sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'], marker='o', color='green',
    # label='ΒΑΣΙΛΟΠΟΥΛΟΣ')
    # plt.scatter(range(len(sql_answer)), sql_answer['TIMH Care Market'], marker='o',
    # color='black', label='Care Market')
    plt.grid(True, alpha=0.2)
    plt.legend()
    plt.savefig('images/bazaar_views.png')
    # plt.show()
    plt.close()