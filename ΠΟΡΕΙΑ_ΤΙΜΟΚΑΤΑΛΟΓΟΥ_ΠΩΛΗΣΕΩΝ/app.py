#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ import sql_select, excel_export, timokatalogos
from Private import sql_connect, slack_app
import matplotlib.pyplot as plt
import numpy as np

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# -------------------- STATEMENTS HERE --------------------
choose = timokatalogos.lista_2020[-1]
from_date = choose.start
to_date = choose.end
id = choose.id

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{id}.xlsx'

# -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ --------------------
timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

# -------------------- READ SALES --------------------
sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                          sql_connect.sql_cnx())

# -------------------- MERGE RESULTS --------------------
final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
    by=['SalesQuantity'])

# --------------------GROUP BY BRANDS TO SLACK --------------------
brand_sales = final_result[['BRAND', 'SalesQuantity', 'Turnover']].groupby(by='BRAND').sum() \
    .sort_values('BRAND').reset_index()


# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(path_to_file, final_result)

# -------------------- SLACK BOT --------------------
report = f"""
>ΠΟΡΕΙΑ ΠΩΛΗΣΕΩΝ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ:
` ΣΥΜΜΕΤΕΧΟΥΝ: \t {len(final_result)} ΠΡΟΪΟΝΤΑ `
` DATERANGE: \t ΑΠΟ: {from_date.strftime("%d-%m-%Y")} \t ΕΩΣ: {to_date.strftime("%d-%m-%Y")} `
` ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ: \t {final_result.SalesQuantity.sum()} TEM `
` ΤΖΙΡΟΣ ΠΩΛΗΣΕΩΝ: \t {round(final_result.Turnover.sum(), 2)} € `
` Α/Α ΕΝΕΡΓΕΙΑ: {choose.id}`
` {choose.comments}`
```{brand_sales}```
"""

slack_app.send_text(report,slack_app.channels[0])
slack_app.send_files(f'{id}.xlsx', path_to_file, 'xlsx', slack_app.channels[0])


# -------------------- PLOT --------------------
plt.figure(figsize=(15, 9))
plt.subplot(xlabel='Brand', title= choose.comments)
plt.bar(brand_sales.BRAND, brand_sales.Turnover, alpha=0.5, color='red', label='ΤΖΙΡΟΣ')
plt.plot(brand_sales.BRAND, brand_sales.SalesQuantity, alpha=0.5, color='blue', label='ΠΟΣΟΤΗΤΑ', marker='o', linestyle="None")
plt.grid(True, alpha=0.8)
plt.legend()
plt.savefig('views.png')
plt.show()

slack_app.send_files('views.png', 'views.png', 'png', slack_app.channels[0])