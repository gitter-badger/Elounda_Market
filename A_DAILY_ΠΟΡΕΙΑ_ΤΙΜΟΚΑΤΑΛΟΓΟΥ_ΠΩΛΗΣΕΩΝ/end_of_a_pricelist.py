#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from pathlib import Path
from A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ.library import end_of_pricelist_excel_export, sql_select, timokatalogos
from Private import sql_connect, slack_app
from datetime import datetime as dt

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- STATEMENTS HERE --------------------
pick_timokatalogo = timokatalogos.lista_2020[-1]
to_date = pick_timokatalogo.end

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]
path_to_file = BASE_DIR / f'A_DAILY_ΠΟΡΕΙΑ_ΤΙΜΟΚΑΤΑΛΟΓΟΥ_ΠΩΛΗΣΕΩΝ/excel/{to_date.strftime("%d-%m")}.xlsx'

# -------------------- TAKE TIMESTAMP --------------------
start_timestamp = dt.now().strftime('%d-%m %H:%M:%S')

# -------------------- ΔΙΑΒΑΖΩ ΤΟΝ ΤΙΜΟΚΑΤΑΛΟΓΟ SQL DB--------------------
timokatalogos = pd.read_sql_query(sql_select.get_ending_pricelist_products(to_date), sql_connect.connect())

# -------------OPEN FILE | WRITE ----------------------------
end_of_pricelist_excel_export.export(path_to_file, timokatalogos[['ΠΕΡΙΓΡΑΦΗ', 'ΚΩΔΙΚΟΣ', 'BRAND']])

# -------------------- SLACK BOT ADD TEXT --------------------
report = f"""
>EKTAKTO ΔΗΜΟΣΙΕΥΜΑ
>ΛΗΞΗ ΤΙΜΟΚΑΤΑΛΟΓΟΥ: {to_date.strftime('%d-%m')}
>
>Data Science Tools Used:
>:slack: :github: :docker: :kubernetes: :python: :javascript: :nodejs: :react: :vue: :fbwow: 
"""
slack_app.send_text(report, slack_app.channels[4])

# -------------------- SLACK BOT ADD FILES --------------------
slack_app.send_files(f'{to_date.strftime("%d-%m")}.xlsx', path_to_file, 'xlsx', slack_app.channels[4])