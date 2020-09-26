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

# sales_cost['S ELOUNDA MARKET'] = sales_cost['SALES ELOUNDA MARKET'].astype(str) + 'EUR - ' + \
#                                  sales_cost['COST ELOUNDA MARKET'].astype(str) + 'EUR'
#
# sales_cost['Q ELOUNDA MARKET'] = sales_cost['Q ELOUNDA MARKET'].astype(str) + 'TEM - ' + \
#                                  sales_cost['COST Q ELOUNDA MARKET'].astype(str) + 'TEM'
#
# sales_cost['S LATO 01'] = sales_cost['SALES LATO 01'].astype(str) + 'EUR - ' + \
#                           sales_cost['COST LATO 01'].astype(str) + 'EUR'
#
# sales_cost['Q LATO 01'] = sales_cost['Q LATO 01'].astype(str) + 'TEM - ' + \
#                           sales_cost['COST Q LATO 01'].astype(str) + 'TEM'
#
# sales_cost['S LATO 02'] = sales_cost['SALES LATO 02'].astype(str) + 'EUR - ' + \
#                           sales_cost['COST LATO 02'].astype(str) + 'EUR'
#
# sales_cost['Q LATO 02'] = sales_cost['Q LATO 02'].astype(str) + 'TEM - ' + \
#                           sales_cost['COST Q LATO 02'].astype(str) + 'TEM'
#
# sales_cost['S LATO 03'] = sales_cost['SALES LATO 03'].astype(str) + 'EUR - ' + \
#                           sales_cost['COST LATO 03'].astype(str) + 'EUR'
#
# sales_cost['Q LATO 03'] = sales_cost['Q LATO 03'].astype(str) + 'TEM - ' + \
#                           sales_cost['COST Q LATO 03'].astype(str) + 'TEM'
#
# sales_cost['S LATO 04'] = sales_cost['SALES LATO 04'].astype(str) + 'EUR - ' + \
#                           sales_cost['COST LATO 04'].astype(str) + 'EUR'
#
# sales_cost['Q LATO 04'] = sales_cost['Q LATO 04'].astype(str) + 'TEM - ' + \
#                           sales_cost['COST Q LATO 04'].astype(str) + 'TEM'
#
# sales_cost['ΠΩΛΗΣΕΙΣ / ΑΓΟΡΕΣ (ΤΖΙΡΟΣ)'] = sales_cost['TurnOver'].astype(str) + 'EUR - ' + \
#                                            sales_cost['SUM COST'].astype(str) + 'EUR'
#
# sales_cost['ΠΩΛΗΣΕΙΣ / ΑΓΟΡΕΣ (ΠΟΣΟΤΗΤΑ)'] = sales_cost['Sales_Quantity'].astype(str) + 'TEM - ' + \
#                                              sales_cost['COST QUANTITY'].astype(str) + 'TEM'
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
