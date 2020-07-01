#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from C_MONTHLY_REPORTS.SQL import sql_vardas
from Private import sql_connect, slack_app
import pandas as pd
from datetime import datetime

today = datetime.now()
dates = pd.date_range('2018-11-1', today)
dates = dates[(dates.strftime('%a') == 'Mon') | (dates.strftime('%a') == 'Tue')]
x = []
for date in dates:
    date = date.strftime('%Y-%m-%d')
    x.append(date)

z = (pd.read_sql_query(sql_vardas.get_vardas_sale(tuple(x)), sql_connect.sql_cnx()))


class Pistotika:
    def __init__(self, date, aitiologia, amount):
        self.date = date
        self.aitiologia = aitiologia
        self.amount = amount

    def __str__(self):
        return f"""
>ΗΜΕΡΟΜΗΝΙΑ: {self.date}
>ΑΙΤΙΟΛΟΓΙΑ: {self.aitiologia}
>ΚΑΘΑΡΟ ΠΟΣΟ ΠΙΣΤΩΣΗΣ: {self.amount} EYR
        """

a = Pistotika(date=datetime(2019, 8, 31), aitiologia='ΕΚΠΤΩΣΗ ΑΠΟ ΝΟΕΜΒΡΙΟ- ΙΟΥΛΙΟ 2019 ΓΙΑ ΛΕΥΚΟ ΨΩΜΙ', amount=201.96)

price = 0.06
money_back = [a.amount]
tziros = price * z.SalesQuantity[0]
print(round(tziros - sum(money_back), 2))

text = f"""
> ΜΗΝΙΑΙΟ ΔΗΜΟΣΙΕΥΜΑ
> ΕΜΜΑΝΟΥΗΛ ΒΑΡΔΑΣ
> ΠΙΣΤΩΤΙΚΟ ΕΚΠΤΩΣΗΣ ΓΙΑ ΤΗΝ ΠΡΟΣΦΟΡΑ ΠΟΥ ΒΑΖΟΥΜΕ ΚΑΘΕ ΔΕΥΤΕΡΑ ΚΑΙ ΤΡΙΤΗ
> ΑΝΑΛΥΣΗ ΠΩΛΗΣΕΩΝ
```{z}```
> ΣΥΜΦΩΝΙΑ: 0.06 EUR ΓΙΑ ΚΑΘΕ ΤΕΜΑΧΙΟ ΠΟΥ ΠΟΥΛΑΜΕ
> ΥΠΟΛΟΓΙΣΜΟΣ: {price} EUR * {z.SalesQuantity[0]} TEM = {tziros} EUR
> ΠΙΣΤΩΤΙΚΑ ΠΟΥ ΕΧΟΥΜΕ ΛΑΒΕΙ:
{a}
> ΚΑΘΑΡΟ ΥΠΟΛΟΙΠΟ ΓΙΑ ΕΩΣ ΣΗΜΕΡΑ:
` {tziros} - {tuple(money_back)} = {round(tziros - sum(money_back), 2)} EUR`
"""

slack_app.send_text(text,slack_app.channels[4])



