#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import os
import sys
import pandas as pd
from Private import sql_connect
from DISCORD.PRE_COST_CALCULATION import excel_export, sql_select, slack
from datetime import datetime as dt

# number here 4018 4002


def run(input_param, get_year):
    order_types = ['ΔΕΑ', 'ΑΔΠ', 'ΑΤΔ', 'ΠΠΡ', 'ΑΠ_ΜΟΒ']
    order_type = order_types[0]  # 0 = ΔΕΑ / 1 = ΑΔΠ ...
    detailed = 'detailed_{}.xlsx'.format(input_param)
    # ------------- ΕΠΙΛΟΓΗ ΥΠΟΚΑΤΑΣΤΗΜΑΤΟΣ ΜΕ ΒΑΣΗ ΤΟ ID ΤΟΥ SCANNER ----------------------------

    def katastima():
        if answer_02.ID[0] in ['00', '01']:
            return 'ΚΕΝΤΡΙΚΑ ΕΔΡΑΣ (ΣΧΙΣΜΑ ΕΛΟΥΝΤΑΣ)'
        elif answer_02.ID[0] == '10':
            return 'ΛΑΤΟ 01 (ΑΚΤΗ ΙΩΣΗΦ ΚΟΥΝΔΟΥΡΟΥ 11)'
        elif answer_02.ID[0] == '20':
            return 'ΛΑΤΟ 02 (28ΗΣ ΟΚΤΩΒΡΙΟΥ 6)'
        elif answer_02.ID[0] == '30':
            return 'ΛΑΤΟ 03 (ΑΓ. ΙΩΑΝΝΗΣ 29)'

    # ------------- ANSWERS ----------------------------
    answer_01 = pd.read_sql_query(sql_select.sql_query(input_param, order_type), sql_connect.connect())
    answer_02 = pd.read_sql_query(sql_select.data_querry(input_param, order_type), sql_connect.connect())

    # -------------------- BARCODES --------------------
    barcodes = answer_01['BarCode']

    # -------------------- SUPPLIER --------------------
    supplier = answer_02.Name[0]
    # Αν δεν βρεθεί όνομα να οριστεί το order_type για να εκτελεστεί στην συνέχεια άλλο ερώτημα στην DB
    if not supplier:
        order_type = 'ΑΠ_ΜΟΒ'
    # -------------------- GET TOP 1 COST FOR EVERY BARCODE --------------------
    answer_03 = pd.DataFrame()

    for counter, barcode in enumerate(barcodes):
        percent = int((100 * (counter + 1)) / len(barcodes))
        filler = "█" * percent
        remaining = '-' * (100 - percent)
        print(f'\r01: CHECKING BARCODE: [{barcode}] \t{counter + 1}/{len(barcodes)} \tComplete:[{filler}{remaining}]{percent}%',
              end='', flush=True)
        if order_type == 'ΑΠ_ΜΟΒ':
            temp = pd.read_sql_query(sql_select.get_product_cost_with_no_name(barcode, get_year), sql_connect.connect())
            if temp.empty:
                temp = pd.read_sql_query(sql_select.get_product_cost_with_no_name(barcode, dt.now().year),
                                         sql_connect.connect())
            answer_03 = answer_03.append(temp)
        else:
            temp = pd.read_sql_query(sql_select.get_product_cost_with_no_name(barcode, get_year), sql_connect.connect())
            if temp.empty:
                temp = pd.read_sql_query(sql_select.get_product_cost_with_no_name(barcode, dt.now().year),
                                         sql_connect.connect())
            answer_03 = answer_03.append(temp)

    # -------------------- MERGE RESULTS --------------------
    final_result = pd.merge(left=answer_01, right=answer_03, left_on='BarCode', right_on='BarCode', how='left').sort_values(
        by=['Περιγραφή'])

    # -------------------- QUANTITY * PRICE --------------------
    final_result['SUM'] = final_result['Ποσότητα'] * final_result['ΚΑΘΑΡΗ ΤΙΜΗ']

    print('\n\n02: Dataframe Merge:\t [✔️]')

    # ----------------FILE PATHS----------------------------
    detailed_file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{k}/{s}/{f}'.format(s=supplier, f=detailed,
                                                                                                  k=katastima())
    # ----------------DIRECTORY PATH ----------------------------
    directory_path = f'/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{katastima()}/{supplier}'

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

    # -------------OPEN FILE | WRITE ----------------------------
    excel_export.export(detailed_file_path, final_result, answer_02, katastima)

    print('\n04: Export To Excel:\t [✔️]')

    # ----------------SLACK BOT CHAT----------------------------
    slack.run(supplier, katastima, final_result, get_year, detailed, detailed_file_path)
