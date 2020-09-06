#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.PRICE_HISTORY import plot, slack, sql
import pandas as pd
import sys
import os
"""Αυτό το πρόγραμμα θέλουμε να δέχεται μια τιμή {BARCODE} και να εξάγει ένα γράφημα 
με το ιστορικό των τιμών του

Από τα παραστατικά που έχουν ΒΗΜΑ "ΑΠΟΔΟΣΗ" θα λαμβάνει τα Barcode. 

Έτσι για κάθε παραστατικό θα φτιάχνουμε και έναν φάκελο
όπου μέσα θα είναι τα γραφήματα.
"""


# Δέχομαι την τιμή {BARCODE} ως είσοδο στην function μου.

def run():
    query = pd.read_sql(sql.get_codes(), sql_connect.sql_cnx())
    folder = query.DocumentCode.unique()
    for document in folder:
        # ----------------DIRECTORY PATH ----------------------------
        directory_path = f'/Users/kommas/OneDrive/Business_Folder/Slack/Supplier_Check/history/{document}'
        target = query[query.DocumentCode == document]
        # -------------------- MAKE DIRECTORY IF DOES NOT EXISTS --------------------
        try:
            print('\n03: Path Check: ', end='')
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
                print('!NEW!\t [✔️]')
            else:
                print('\t\t [✔️]')
        except OSError:
            print("!ERROR! [❌️]")
            sys.exit(1)

        for i, barcode in enumerate(target.BarCode):
            percent = int((100 * (i + 1)) / len(target.BarCode))
            filler = "█" * (percent // 2)
            remaining = '-' * ((100 - percent) // 2)
            df = pd.read_sql(sql.get_product_cost(barcode), sql_connect.sql_cnx())
            plot.run(df, barcode, directory_path)
            print(f'\rDONE:[{filler}{remaining}]{percent}%', end='', flush=True)
        slack.run(document)


