#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from datetime import datetime
from ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ import sql_select, excel_export
from Private import sql_connect, slack_app
import matplotlib.pyplot as plt
import numpy as np
# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- STATEMENTS HERE --------------------
from_date = datetime(2020, 6, 1)  # Αλλάζω το ημερομηνιακό διάστημα από
to_date = datetime(2020, 6, 15)  # έως. Πρέπει να είναι ακριβώς
month = datetime.today().strftime('%y_%m')
# month = '20_02' # custom

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{month}.xlsx'

# -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ --------------------
timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

# -------------------- READ SALES --------------------
sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                          sql_connect.sql_cnx())

# -------------------- MERGE RESULTS --------------------
final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(
    by=['SalesQuantity'])

# --------------------BRANDS --------------------
brands = final_result['BRAND'].unique()
# TODO για κάθε Brand αναλυτική εξαγωγή στο EXCEL
# TODO για όλα τα BRAND μια συνοπτική εικόνα

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(path_to_file, final_result)

# -------------------- SLACK BOT --------------------
report = f"""
||
ΠΩΛΗΣΕΙΣ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ 15 ΗΜΕΡΩΝ
ΣΥΜΜΕΤΕΧΟΥΝ: \t {len(final_result)} ΠΡΟΪΟΝΤΑ
DATERANGE: \t ΑΠΟ: {from_date.strftime("%d-%m-%Y")} \t ΕΩΣ: {to_date.strftime("%d-%m-%Y")}
ΠΟΣΟΤΗΤΑ ΠΩΛΗΣΕΩΝ: \t {final_result.SalesQuantity.sum()} TEM 
ΤΖΙΡΟΣ ΠΩΛΗΣΕΩΝ: \t {round(final_result.Turnover.sum(), 2)} €
||
"""

slack_app.post_message_to_slack(report)
print(report)

# -------------------- SALES QUANTITY --------------------
sales_quantity = final_result.SalesQuantity.values

# -------------------- QUARTILES --------------------
quartiles = np.quantile(sales_quantity, [.25, .5, .75])

# -------------------- PLOT --------------------
plt.figure(figsize=(15, 9))
plt.subplot(1,2,1, xlabel='Products', ylabel='Quantity Sales', title=f'[Histogram (Quartiles)]')
plt.hist(sales_quantity)
plt.axvline(x=quartiles[0], label=f"Q1={quartiles[0]}", c ='#6400e4')
plt.axvline(x=quartiles[1], label=f"Q2={quartiles[1]}", c ='#fd4d3f')
plt.axvline(x=quartiles[2], label=f"Q3={quartiles[2]}", c ='#4fe0b0')

plt.subplot(1, 2, 2, xlabel='BoxPlot', ylabel='Quantity Sales', title='Quantity [Box Plot]')
plt.boxplot(sales_quantity)
plt.grid(True, alpha=0.2)
# plt.legend()
plt.savefig('views.png')
plt.show()
