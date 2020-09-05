#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import matplotlib.pyplot as plt


def run(df, barcode):
    X = df['ΗΜΕΡΟΜΗΝΙΑ']
    y = df['ΚΑΘΑΡΗ ΤΙΜΗ']
    plt.figure(figsize=(15, 9))
    plt.subplot(xlabel='ΕΤΟΣ', ylabel='TIMH', title=f'ΙΣΤΟΡΙΚΟ ΤΙΜΗΣ ΕΙΔΟΥΣ: {df["ΠΕΡΙΓΡΑΦΗ"].unique()} : BARCODE:[{barcode}]')
    colors = [plt.cm.Spectral(i / float(len(X))) for i in range(len(X))]
    plt.scatter(X, y, alpha=0.8, color=colors, marker='o')
    plt.grid(True, alpha=0.5)
    plt.savefig('images/price_history.png')
    # plt.show()
    plt.close()

