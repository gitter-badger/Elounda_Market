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
` Α/Α ΤΙΜΟΚΑΤΑΛΟΓΟΥ ΓΙΑ ΤΟ ΕΤΟΣ: {choose.id}`
` {choose.comments}`
```{brand_sales}```
"""

# slack_app.post_message_to_slack(report)
print(report)

# -------------------- SALES QUANTITY --------------------
sales_quantity = final_result.SalesQuantity.values

# -------------------- QUARTILES --------------------
quartiles = np.quantile(sales_quantity, [.25, .5, .75])

# -------------------- PLOT --------------------
plt.figure(figsize=(15, 9))
plt.subplot(1, 2, 1, xlabel='Products', ylabel='Quantity Sales', title=f'[Histogram (Quartiles)]')
plt.hist(sales_quantity)
plt.axvline(x=quartiles[0], label=f"Q1={quartiles[0]}", c='#6400e4')
plt.axvline(x=quartiles[1], label=f"Q2={quartiles[1]}", c='#fd4d3f')
plt.axvline(x=quartiles[2], label=f"Q3={quartiles[2]}", c='#4fe0b0')
plt.legend()
plt.subplot(1, 2, 2, xlabel='BoxPlot', ylabel='Quantity Sales', title='Quantity [Box Plot]')
plt.boxplot(sales_quantity)
plt.grid(True, alpha=0.2)
# plt.legend()
plt.savefig('views.png')
plt.show()
