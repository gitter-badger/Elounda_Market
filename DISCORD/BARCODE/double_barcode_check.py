#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

from Private import sql_connect
from DISCORD.BARCODE import excel, slack, database
import pandas as pd

def run():
    output_file = 'Double_Barcodes.xlsx'
    path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
    barcode_old_values = ('5200116140910', '5206586230687', '5213002921425', '5214000237334')

    # Assign the SQL Query Answer
    sql_answer = pd.read_sql_query(database.sql_query(), sql_connect.sql_cnx())

    sql_answer['Υπάρχει στο Slack'] = sql_answer.BarCode.apply(lambda x: 'NAI' if x in barcode_old_values else 'OXI')

    print('DATA EXPORT PREVIEW')
    print()
    print(sql_answer)
    print()

    # Εισαγωγή Δεομένων στο  EXCEL
    excel.export(path_to_file, sql_answer)

    # SLACK
    slack.app(sql_answer)