#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
import numpy as np
from DISCORD.BAZAAR import excel, scrap, slack, sql, plot
from Private import sql_connect


def run():
    # -------------------- Statements Here --------------------
    output_file = 'Bazaar.xlsx'
    path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
    mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
    mail_names = ['Τιμολόγιο Bazaar (Κομμάς)', 'Τιμολόγιο Bazaar (Λογιστήριο)', 'Τιμολόγιο Bazaar (Κατάστημα)']
    main_name = 'Bazaar A.E.'
    # -------------------- Assign the SQL Query Answer --------------------
    sql_answer_bazaar = pd.read_sql_query(sql.private_database_query(main_name), sql_connect.sql_cnx())

    unique_brands = sql_answer_bazaar['BRAND'].unique()
    markup_per_brand= [round(sql_answer_bazaar['ΚΕΡΔΟΦΟΡΙΑ'][sql_answer_bazaar['BRAND'] == i].mean() * 100, 2) for i in unique_brands]

    # -------------------- ASSIGN VALUES HERE MARKUP / QUARTILES --------------------
    markup = round(sql_answer_bazaar['ΚΕΡΔΟΦΟΡΙΑ'] * 100, 2)
    quartiles = np.quantile(markup, [.25, .5, .75])
    order_id = sql_answer_bazaar['ΠΑΡΑΣΤΑΤΙΚΟ'].unique()
    retail_price = sql_answer_bazaar['ΤΙΜΗ ΛΙΑΝΙΚΗΣ']
    retail_q = np.quantile(retail_price, [.25, .5, .75])

    # -------------------- FIND BARCODES WHO ARE IN EVERY QUARTILE --------------------
    codes_in_q1 = sql_answer_bazaar[markup <= quartiles[0]]
    codes_in_q2 = sql_answer_bazaar[(markup > quartiles[0]) & (markup <= quartiles[1])]
    codes_in_q3 = sql_answer_bazaar[(markup > quartiles[1]) & (markup <= quartiles[2])]
    codes_in_q4 = sql_answer_bazaar[markup > quartiles[2]]

    # -------------------- Make the list to query for every barcode in bazaar web page --------------------
    barcode_lista = sql_answer_bazaar['BARCODE']
    scrap.shops = [scrap.a, scrap.b, scrap.e]
    out = scrap.calculate_prices(barcode_lista)

    # -------------------- Assign the results --------------------
    sql_answer_bazaar['ΤΙΜΗ BAZAAR'] = out['BAZAAR']
    sql_answer_bazaar['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'] = out['ΑΒ. Βασιλόπουλος']
    sql_answer_bazaar['TIMH Care Market'] = out['Care Market']

    # -------------------- EXTRA RETAIL/BAZAAR -------------------
    extra = sql_answer_bazaar
    extra['DIFFERENCE'] = 0
    extra['DIFFERENCE'] = round((extra['ΤΙΜΗ ΛΙΑΝΙΚΗΣ'] / extra['ΤΙΜΗ BAZAAR'] -1)* 100, 2)
    extra['DIFFERENCE'] = extra['DIFFERENCE'].replace(to_replace=-100.00, value=np.nan)
    extra['DIFFERENCE'] = extra['DIFFERENCE'].replace([np.inf, -np.inf], np.nan)
    extra = extra.dropna()
    extra = extra.sort_values(by='DIFFERENCE')

    # -------------------- PLOT A HISTOGRAM WITH QUARTILE VALUES --------------------
    plot.run(sql_answer_bazaar, retail_price)
    plot.run_02(markup_per_brand, unique_brands)
    plot.run_03(extra['BARCODE'], extra['DIFFERENCE'])

    # -------------------- Εισαγωγή Δεομένων στο  EXCEL --------------------
    excel.export(path_to_file, sql_answer_bazaar)

    # -------------------- PLUS STATS --------------------
    sql_answer_bazaar['cost'] = round(sql_answer_bazaar['ΚΑΘΑΡΗ ΤΙΜΗ'] * sql_answer_bazaar['ΠΟΣΟΤΗΤΑ'], 2)
    sql_answer_bazaar['elounda_sales'] = round(sql_answer_bazaar['ΤΙΜΗ ΛΙΑΝΙΚΗΣ'] * sql_answer_bazaar['ΠΟΣΟΤΗΤΑ'], 2)
    sql_answer_bazaar['bazaar_sales'] = round(sql_answer_bazaar['ΤΙΜΗ BAZAAR'] * sql_answer_bazaar['ΠΟΣΟΤΗΤΑ'], 2)

    cost = round(sql_answer_bazaar['cost'].sum(), 2)
    elounda_sales = round(sql_answer_bazaar['elounda_sales'].sum(), 2)
    bazaar_sales = round(sql_answer_bazaar['bazaar_sales'].sum(), 2)
    kerdos_elounda = round(elounda_sales - cost, 2)
    kerdos_bazaar = round(bazaar_sales - cost, 2)

    # ----------------SLACK BOT----------------------------
    slack.run(order_id, output_file, path_to_file, cost, elounda_sales, kerdos_elounda, bazaar_sales, kerdos_bazaar)

