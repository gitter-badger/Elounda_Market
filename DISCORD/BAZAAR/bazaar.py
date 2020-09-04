#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from DISCORD.BAZAAR import excel, scrap, slack, sql, plot
from Private import  sql_connect

# -------------------- Statements Here --------------------
output_file = 'Bazaar.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Τιμολόγιο Bazaar (Κομμάς)', 'Τιμολόγιο Bazaar (Λογιστήριο)', 'Τιμολόγιο Bazaar (Κατάστημα)']
main_name = 'Bazaar A.E.'


def run():
    # -------------------- Assign the SQL Query Answer --------------------
    sql_answer = pd.read_sql_query(sql.private_database_query(main_name), sql_connect.sql_cnx())

    # -------------------- ASSIGN VALUES HERE MARKUP / QUARTILES --------------------
    markup = round(sql_answer['ΚΕΡΔΟΦΟΡΙΑ'] * 100, 2)
    quartiles = np.quantile(markup, [.25, .5, .75])
    order_id = sql_answer['ΠΑΡΑΣΤΑΤΙΚΟ'].unique()
    retail_price = sql_answer['ΤΙΜΗ ΛΙΑΝΙΚΗΣ']
    retail_q = np.quantile(retail_price, [.25, .5, .75])

    # -------------------- FIND BARCODES WHO ARE IN EVERY QUARTILE --------------------
    codes_in_q1 = sql_answer[markup <= quartiles[0]]
    codes_in_q2 = sql_answer[(markup > quartiles[0]) & (markup <= quartiles[1])]
    codes_in_q3 = sql_answer[(markup > quartiles[1]) & (markup <= quartiles[2])]
    codes_in_q4 = sql_answer[markup > quartiles[2]]

    # -------------------- Make the list to query for every barcode in bazaar web page --------------------
    lista = sql_answer['BARCODE']
    scrap.shops = [scrap.a, scrap.b, scrap.e]
    out = scrap.calculate_prices(lista)

    # -------------------- Assign the results --------------------
    sql_answer['ΤΙΜΗ BAZAAR'] = out['BAZAAR']
    sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'] = out['ΑΒ. Βασιλόπουλος']
    sql_answer['TIMH Care Market'] = out['Care Market']

    # -------------------- PLOT A HISTOGRAM WITH QUARTILE VALUES --------------------
    plot.run(sql_answer, retail_price)

    # -------------------- Εισαγωγή Δεομένων στο  EXCEL --------------------
    excel.export(path_to_file, sql_answer)

    # ----------------SLACK BOT----------------------------
    slack.run(order_id, output_file, path_to_file)
