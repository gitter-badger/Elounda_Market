#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt

# ----------------MAKE DF Reports Viewable----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class EShop():
    def __init__(self, webpage, price_tag, name, extra=''):
        self.webpage = webpage
        self.price_tag = price_tag
        self.name = name
        self.extra = extra
        self.prices = []
        self.barcodes = []

    def __str__(self):
        return self.name

    def scrap_data(self, data):
        names = ['Care Market']
        webpage_response = requests.get(f'{self.webpage}{data}{self.extra}')
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, "html.parser")
        try:
            final_price = soup.select(self.price_tag)[0].get_text()
        except IndexError:
            final_price = '0.00'
        if self.name in names:
            final_price = final_price[:5]
        final_price = final_price.replace('€', '')
        final_price = final_price.strip()
        final_price = final_price.replace(',', '.')
        final_price = float(final_price)
        return self.prices.append(final_price)


a = EShop(webpage='https://www.bazaar-online.gr/search-products/?search-for=',
          price_tag='.current-price',
          name='BAZAAR')

b = EShop(webpage='https://www.ab.gr/click2shop/search?q=',
          price_tag='.quantity-price',
          name='ΑΒ. Βασιλόπουλος')

c = EShop(webpage='https://www.market4u.gr/?s=',
          price_tag='.price',
          name='Market 4 you',
          extra='&post_type=product')

d = EShop(webpage='https://www.thanopoulos.gr/el/search?search_query=',
          price_tag='.product-price',
          name='Δημήτριος Θανόπουλος')

e = EShop(webpage='https://www.caremarket.gr/apotelesmata-anazitisis/?Query=',
          price_tag='.price',
          name='Care Market')


# For Testing
shops = [a, b, c, d, e]
barcode_list = [5201156933227]


df = pd.DataFrame()


def calculate_prices(in_barcode_list):
    for shop in shops:
        # print(f'{shop} Start: {dt.now().strftime("%H:%M:%S")}')
        for barcode in in_barcode_list:
            shop.scrap_data(barcode)
            shop.barcodes.append(barcode)
            print(f'{shop}: {barcode}: Start: {dt.now().strftime("%H:%M:%S")}')
        df[shop.name] = shop.prices
    return df

# print(calculate_prices(barcode_list))