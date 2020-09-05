#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from Private import sql_connect
from DISCORD.PRICE_HISTORY import plot, slack, sql
import pandas as pd
"""Αυτό το πρόγραμμα θέλουμε να δέχεται μια τιμή {BARCODE} και να εξάγει ένα γράφημα 
με το ιστορικό των τιμών του
"""


# Δέχομαι την τιμή {BARCODE} ως είσοδο στην function μου.
def run(barcode):
    df = pd.read_sql(sql.get_product_cost(barcode), sql_connect.sql_cnx())
    plot.run(df, barcode)
    result = df['ΚΑΘΑΡΗ ΤΙΜΗ'].unique()
    return result


