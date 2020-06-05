#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from datetime import datetime
from Pricelist_Sales_Ongoing import  sql_select
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
final_result = pd.merge(left=timokatalogos, right=sales, left_on='ΚΩΔΙΚΟΣ', right_on='ΚΩΔΙΚΟΣ')

# -------------------- IMPORT DATA TO EXCEL --------------------
with pd.ExcelWriter(path_to_file, engine='xlsxwriter', datetime_format='dd - mm - yyyy') as writer:
    final_result.to_excel(writer, sheet_name='TODAY', startcol=0, startrow=0, index=None)

    # Φτιάχνω το excel για να είναι ευαναγνωστο
    workbook = writer.book
    worksheet = writer.sheets['TODAY']
    number = workbook.add_format({'num_format': '€#,##0.00',
                                  'align': 'left',
                                  'bold': False,
                                  "font_name": "Avenir Next"})

    normal = workbook.add_format({'align': 'left',
                                  'bold': False,
                                  "font_name": "Avenir Next"})

    bold = workbook.add_format({'color': 'red',
                                'align': 'left',
                                'bold': True,
                                "font_name": "Avenir Next"})

    worksheet.set_column('A:A', 10, normal)
    worksheet.set_column('B:B', 10, normal)
    worksheet.set_column('C:C', 12, normal)
    worksheet.set_column('D:D', 12, normal)
    worksheet.set_column('E:E', 50, normal)
    worksheet.set_column('F:F', 15, normal)
    worksheet.set_column('G:G', 12, number)
    worksheet.set_column('H:H', 12, number)
    worksheet.set_column('I:I', 12, normal)
    worksheet.set_column('J:J', 12, normal)
    worksheet.set_column('K:K', 12, number)
    worksheet.set_column('L:L', 12, number)

    # Conditional Formating
    worksheet.conditional_format(f'I1:I{len(final_result) + 1}', {'type': '3_color_scale'})
    worksheet.conditional_format(f'J1:J{len(final_result) + 1}', {'type': '3_color_scale'})
    worksheet.write(len(final_result) + 1, 9, final_result.SalesQuantity.sum(), bold)
    worksheet.write(len(final_result) + 1, 10, final_result.Turnover.sum(), bold)

# -------------------- PRINT TOTAL RESULTS --------------------
report = f"""
ΠΩΛΗΣΕΙΣ ΓΙΑ ΤΙΣ ΠΡΟΣΦΟΡΕΣ 15 ΗΜΕΡΩΝ
DATERANGE   : {from_date.strftime("%d-%m-%Y")} / {to_date.strftime("%d-%m-%Y")}
QUANTITY    : {final_result.SalesQuantity.sum()} TEM 
SALES VALUE : {round(final_result.Turnover.sum(), 2)} €
ΣΥΜΜΕΤΕΧΟΥΝ   : {len(final_result)} ΠΡΟΪΟΝΤΑ
"""

slack_app.post_message_to_slack(report)
print(report)