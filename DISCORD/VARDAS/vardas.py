#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import sql_connect
from DISCORD.VARDAS import slack, sql
import pandas as pd
from datetime import datetime


def run():
    class Supplier:
        def __init__(self, poliseis, pistotika, dates, price, money_back, tziros, ypoloipo):
            self.poliseis = poliseis
            self.pistotika = pistotika
            self.dates = dates
            self.price = price
            self.money_back = money_back
            self.tziros = tziros
            self.ypoloipo = ypoloipo

        def __str__(self):
            return f"""
>:python: :  ΜΗΝΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ [ΕΜΜΑΝΟΥΗΛ ΒΑΡΔΑΣ (ΠΕΚ)] (0.06 EUR * ΠΟΣΟΤΗΤΑ) - (ΑΘΡΟΙΣΜΑ ΠΙΣΤΩΤΙΚΩΝ)
>ΠΩΛΗΣΕΙΣ:
```{self.poliseis}```
>ΠΙΣΤΩΤΙΚΑ:
```{pistotika}```
>ΚΑΘΑΡΟ ΥΠΟΛΟΙΠΟ:
` {self.tziros} - {self.money_back} = {self.ypoloipo} EUR`
>:fbwow:
    """


    today = datetime.now()
    dates = pd.date_range('2018-11-1', today)
    dates = dates[(dates.strftime('%a') == 'Mon') | (dates.strftime('%a') == 'Tue')]
    x = []
    for date in dates:
        date = date.strftime('%Y-%m-%d')
        x.append(date)

    poliseis = pd.read_sql_query(sql.get_vardas_sale(tuple(x)), sql_connect.sql_cnx())
    pistotika = pd.read_sql_query(sql.pistotiko(), sql_connect.sql_cnx())

    price = 0.06
    money_back = round(sum(pistotika['NET VALUE']), 2)
    tziros = round(price * poliseis.SalesQuantity[0], 2)
    ypoloipo = round(tziros - money_back, 2)

    vardas = Supplier(poliseis, pistotika, dates, price, money_back, tziros, ypoloipo)

    slack.run(vardas)

