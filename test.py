#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.figure(figsize=(15, 9))
plt.subplot(title='Retail Price [Scatter Plot]')
plt.pie(payment_method_freqs,
        autopct='%d%%',
        labels=payment_method_names)
plt.axis('equal')

plt.show()
