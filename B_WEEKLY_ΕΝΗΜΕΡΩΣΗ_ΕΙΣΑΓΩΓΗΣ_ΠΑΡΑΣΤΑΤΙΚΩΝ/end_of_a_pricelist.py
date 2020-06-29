#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from B_WEEKLY_ΕΝΗΜΕΡΩΣΗ_ΕΙΣΑΓΩΓΗΣ_ΠΑΡΑΣΤΑΤΙΚΩΝ.Libraries import sql_import_report, excel_export
from Private import sql_connect, slack_app
import matplotlib.pyplot as plt
import time
from datetime import datetime as dt

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- STATEMENTS HERE --------------------
to_date = dt(2020, 6, 30)
path_to_file = f'EXCEL/{to_date.strftime("%d-%m")}.xlsx'

# -------------------- TAKE TIMESTAMP --------------------
start_timestamp = dt.now().strftime('%d-%m %H:%M:%S')

# -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ SQL DB--------------------
timokatalogos = pd.read_sql_query(sql_import_report.get_ending_pricelist_products(to_date), sql_connect.sql_cnx())

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(path_to_file, timokatalogos[['ΠΕΡΙΓΡΑΦΗ', 'ΚΩΔΙΚΟΣ', 'BRAND']])

# -------------------- SLACK BOT ADD TEXT --------------------
report = f"""
>EKTAKTO ΔΗΜΟΣΙΕΥΜΑ
>ΛΗΞΗ ΤΙΜΟΚΑΤΑΛΟΓΟΥ: {to_date.strftime('%d-%m')}
"""
slack_app.send_text(report, slack_app.channels[1])

# -------------------- SLACK BOT ADD FILES --------------------
slack_app.send_files(f'{to_date.strftime("%d-%m")}.xlsx', path_to_file, 'xlsx', slack_app.channels[1])