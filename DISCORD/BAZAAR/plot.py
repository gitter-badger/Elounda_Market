#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def run(sql_answer, retail_price):
    # create your figure here
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='Product', ylabel='Retail Price', title='Retail Price [Scatter Plot]')
    plt.scatter(range(len(sql_answer)), retail_price, marker='x', label='ELOUNDA', alpha=.8)
    plt.scatter(range(len(sql_answer)), sql_answer['ΤΙΜΗ BAZAAR'], marker='o', label='BAZAAR', alpha=.8)
    plt.plot(range(len(sql_answer)), sql_answer['ΚΑΘΑΡΗ ΤΙΜΗ'], label='ΚΑΘΑΡΗ ΤΙΜΗ', alpha=.8)
    # plt.scatter(range(len(sql_answer)), sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'], marker='o', color='green',
    # label='ΒΑΣΙΛΟΠΟΥΛΟΣ')
    # plt.scatter(range(len(sql_answer)), sql_answer['TIMH Care Market'], marker='o',
    # color='black', label='Care Market')
    plt.grid(True, alpha=0.2)
    plt.legend()
    plt.savefig('images/bazaar_views.png')
    # plt.show()
    plt.close()


def run_02(markup_per_brand, unique_brands):
    # create your figure here
    X = unique_brands
    y = markup_per_brand
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='BRAND NAME', ylabel='MARKUP', title='ELOUNDA MARKET MARKUP PER BRAND ')
    plt.xticks(rotation=60)
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.bar(X, y, alpha=0.9, color=colors)
    for a, b in zip(X, y):
        label = "{:.2f}%".format(b)

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.2)
    plt.savefig('images/markup_bazaar_views.png')
    # plt.show()
    plt.close()

def run_03(barcode, diference):
    # create your figure here
    X = barcode
    y = diference
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΚΩΔΙΚΟΣ', ylabel='PERCENT (%)', title='ΠΟΣΟΣΤΟ ΠΡΟΣΑΥΞΗΣΗΣ ΣΕ ΣΧΕΣΗ ΜΕ ΤΗΝ ΤΙΜΗ BAZAAR (RETAIL TO RETAIL) ')
    plt.xticks(rotation=90)
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.bar(X, y, alpha=0.9, color=colors)
    for a, b in zip(X, y):
        label = "{}%".format(int(b))

        # this method is called for each point
        plt.annotate(label,  # this is the text
                     (a, b),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center
    plt.grid(True, alpha=0.2)
    plt.savefig('images/retail_to_retail.png')
    # plt.show()
    plt.close()

