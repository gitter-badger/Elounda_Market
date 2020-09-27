#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from Private import sql_connect
from ΑΓΟΡΕΣ_ΠΩΛΗΣΕΙΣ import sql, excel

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

brand = ('Aphrodite', 'Aphrodite')
year = 2019
sales = pd.read_sql(sql.sales(brand, year), sql_connect.connect())
cost = pd.read_sql(sql.cost(brand, year), sql_connect.connect())

print(sales)
print(cost)

sales_cost = pd.merge(left=sales, right=cost, left_on='BARCODE', right_on='BARCODE').sort_values(
    by=['BARCODE']).reset_index()

output = sales_cost[['BARCODE',
                     'DESCRIPTION',
                     'ΑΓΟΡΕΣ',
                     'ΠΩΛΗΣΕΙΣ',
                     'ΑΓΟΡΕΣ EM',
                     'ΠΩΛΗΣΕΙΣ EM',
                     'ΑΓΟΡΕΣ L1',
                     'ΠΩΛΗΣΕΙΣ L1',
                     'ΑΓΟΡΕΣ L2',
                     'ΠΩΛΗΣΕΙΣ L2',
                     'ΑΓΟΡΕΣ L3',
                     'ΠΩΛΗΣΕΙΣ L3',
                     'ΑΓΟΡΕΣ L4',
                     'ΠΩΛΗΣΕΙΣ L4']]

file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Private_Analytics/sales_cost.xlsx'
excel.run(file_path, output)
