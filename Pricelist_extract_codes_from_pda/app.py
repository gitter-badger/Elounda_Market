#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import date
from Pricelist_extract_codes_from_pda import  sql_select,excel_export
from Private import sql_connect

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- STATEMENTS HERE --------------------
id = 1873           # ΑΥΤΗ Η ΠΑΡΑΜΕΤΡΟΣ ΚΑΘΕ ΦΟΡΑ ΑΛΛΑΖΕΙ
how_many_weeks = 2  # ΑΥΤΗ Η ΠΑΡΑΜΕΤΡΟΣ ΚΑΘΕ ΦΟΡΑ ΑΛΛΑΖΕΙ
price_or_discount= ['Πελάτες Τιμή Πώλησης', 'Πωλήσεις Έκπτωση 1']
output_file = 'Timokatalogos.xlsx'
path_to_file = f'/Users/kommas/OneDrive/{output_file}'

# -------------------- READ PDA SCANNED ITEMS --------------------
sql = pd.read_sql_query(sql_select.pda_results(id), sql_connect.sql_cnx())
df = pd.DataFrame()
today = date.today().strftime('%d/%m/%y')
period = date.today() +  relativedelta(weeks=+how_many_weeks)


repeatable_list = [price_or_discount[1], today, period.strftime('%d/%m/%y'), 1]


sql['Τιμ/γος'] = [repeatable_list[0] for i in range(len(sql))]
sql['Aπό'] = [repeatable_list[1] for i in range(len(sql))]
sql['Εως'] = [repeatable_list[2] for i in range(len(sql))]
sql['Υποκ/μα'] = [repeatable_list[3] for i in range(len(sql))]

# -------------------- IMPORT DATA TO EXCEL --------------------
excel_export.export(path_to_file, sql)

