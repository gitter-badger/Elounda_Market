#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from datetime import datetime
from ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ import  sql_select, excel_export
from Private import sql_connect, slack_app

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
path_to_file = BASE_DIR / f'Pricelist_Sales_Ongoing/excel/{month}.xlsx'

# -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ --------------------
timokatalogos = pd.read_sql_query(sql_select.get_products_in_the_period(from_date, to_date), sql_connect.sql_cnx())

# -------------------- READ SALES --------------------
sales = pd.read_sql_query(sql_select.get_sales(from_date, to_date, tuple(timokatalogos['ΚΩΔΙΚΟΣ'].values)),
                          sql_connect.sql_cnx())

# -------------------- MERGE RESULTS --------------------
final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ').sort_values(by=['SalesQuantity'])

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(path_to_file, final_result)

# -------------------- SLACK BOT --------------------
report = f"""
ΠΩΛΗΣΕΙΣ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ 15 ΗΜΕΡΩΝ
DATERANGE   : {from_date.strftime("%d-%m-%Y")} / {to_date.strftime("%d-%m-%Y")}
QUANTITY    : {final_result.SalesQuantity.sum()} TEM 
SALES VALUE : {round(final_result.Turnover.sum(), 2)} €
ΣΥΜΜΕΤΕΧΟΥΝ   : {len(final_result)} ΠΡΟΪΟΝΤΑ
"""

slack_app.post_message_to_slack(report)
print(report)