#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from DISCORD.SUPPLIER_EVALUATION import slack, sql, plot
from Private import sql_connect

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def run(name, year):
    df = pd.read_sql(sql.run(name, year), sql_connect.connect())
    # print(df)
    grouped_by_store = df.groupby(by='ΥΠΟΚΑΤΑΣΤΗΜΑ').sum().reset_index()
    column_list = ['ΔΕΥΤΕΡΑ', 'ΤΡΙΤΗ', 'ΤΕΤΑΡΤΗ', 'ΠΕΜΠΤΗ', 'ΠΑΡΑΣΚΕΥΗ', 'ΣΑΒΒΑΤΟ', 'ΚΥΡΙΑΚΗ']
    grouped_by_store['ΠΑΡΑΣΤΑΤΙΚΑ'] = grouped_by_store[column_list].sum(axis=1)
    print(grouped_by_store)

    # ΣΕ ΠΟΙΑ ΥΠΟΚΑΤΑΣΤΗΜΑΤΑ ΠΑΡΑΛΑΜΒΑΝΩ ΕΜΠΡΕΥΜΑΤΑ (ΛΙΣΤΑ)
    supply_stores = df['ΥΠΟΚΑΤΑΣΤΗΜΑ'].unique()

    # ΓΙΑ ΚΑΘΕ ΥΠΟΚΑΤΑΣΤΗΜΑ ΒΡΕΣ ΜΟΥ ΤΗΝ ΜΕΣΗ ΤΙΜΗ ΣΤΙΣ ΓΡΑΜΜΕΣ ΚΑΙ ΤΗΝ ΜΕΣΗ ΤΙΜΗ ΓΙΑ ΤΙΣ ΠΟΣΟΤΗΤΕΣ
    supply_lines_mean = []
    supply_quantity_mean = []
    for i in supply_stores:
        supply_lines_mean.append(int((df[df['ΥΠΟΚΑΤΑΣΤΗΜΑ'] == i]['ΓΡΑΜΜΕΣ'].mean())))
        supply_quantity_mean.append(int(df[df['ΥΠΟΚΑΤΑΣΤΗΜΑ'] == i]['ΠΟΣΟΤΗΤΑ'].mean()))
    # print(list(zip(supply_stores, supply_lines_mean)))
    # print(list(zip(supply_stores, supply_quantity_mean)))

    # plot
    plot.plot_sum_values(grouped_by_store['ΥΠΟΚΑΤΑΣΤΗΜΑ'], grouped_by_store['ΧΡΕΩΣΗ'], f'ΥΠΟΚΑΤΑΣΤΗΜΑ ΧΡΕΩΣΗ ΕΤΟΣ:{year}')
    return round(grouped_by_store['ΧΡΕΩΣΗ'].sum(), 2)

# run('Μακριδάκη Α.- Γ.Μακατουνάκης Ο.Ε', 2020)
xreosi_per_year = []
for i in range(2012, 2021):
    print(f'ETOS: {i}')
    xreosi_per_year.append(run('Bazaar A.E.', i))
print(xreosi_per_year)

plot.plot_sum_values(range(2012, 2021), xreosi_per_year, 'ert')