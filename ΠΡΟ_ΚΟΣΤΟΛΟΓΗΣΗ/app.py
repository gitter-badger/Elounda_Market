#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import os
import sys
import pandas as pd
from ΠΡΟ_ΚΟΣΤΟΛΟΓΗΣΗ import excel_export, sql_select
from Private import slack_app, send_mail, sql_connect

# ---------------- MAKE DF REPORT VIEWABLE ----------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# ---------------- STATEMENTS HERE ----------------
order_types = ['ΔΕΑ', 'ΑΔΠ', 'ΑΤΔ']
# TODO 'ΑΠΟ ΕΔΩ'
order_type = order_types[0]  # 0 = ΔΕΑ / 1 = ΑΔΠ ...
input_param = '4002'  # Βάζω
# TODO 'ΕΩΣ ΕΔΩ'
output_file = "temp_{}.xlsx".format(input_param)
detailed = 'detailed_{}.xlsx'.format(input_param)

# ---------------- MAIL LIST ----------------------------
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['ΠΡΟΕΠΙΣΚΟΠΗΣΗ: (Κομμάς)', 'ΠΡΟΕΠΙΣΚΟΠΗΣΗ: (Λογιστήριο)',
              'ΠΡΟΕΠΙΣΚΟΠΗΣΗ: (Κατάστημα)']

# ---------------- Open HTML File for the BODY MAIL ----------------
with open('body.html', 'r') as html_file:
    word = html_file.read()


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
answer_01 = pd.read_sql_query(sql_select.sql_query(input_param, order_type), sql_connect.sql_cnx())
answer_02 = pd.read_sql_query(sql_select.data_querry(input_param, order_type), sql_connect.sql_cnx())

# -------------------- BARCODES --------------------
barcodes = answer_01['BarCode']

# -------------------- SUPPLIER --------------------
supplier = answer_02.Name[0]

# -------------------- GET TOP 1 COST FOR EVERY BARCODE --------------------
answer_03 = pd.DataFrame()
for barcode in barcodes:
    answer_03 = answer_03.append(pd.read_sql_query(sql_select.get_product_cost(barcode,supplier), sql_connect.sql_cnx()))

# -------------------- MERGE RESULTS --------------------
final_result = pd.merge(left=answer_01, right=answer_03, left_on='BarCode', right_on='BarCode', how='left').sort_values(
    by=['Περιγραφή'])

# -------------------- QUANTITY * PRICE --------------------
final_result['SUM'] = final_result['Ποσότητα'] * final_result['ΚΑΘΑΡΗ ΤΙΜΗ']
print(final_result)

# ----------------FILE PATHS----------------------------
file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{k}/{s}/{f}'.format(s=supplier, f=output_file,
                                                                                     k=katastima())
detailed_file_path = '/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{k}/{s}/{f}'.format(s=supplier, f=detailed,
                                                                                              k=katastima())
# ----------------DIRECTORY PATH ----------------------------
directory_path = f'/Users/kommas/OneDrive/Business_Folder/Slack/Orders/{katastima()}/{supplier}'

# -------------------- MAKE DIRECTORY IF DOES NOT EXISTS --------------------
try:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print('!NEW! file path created')
    else:
        print('file path EXISTS')
except OSError:
    print("!ERROR! Creation of the directory FAILED")
    sys.exit(1)

# -------------OPEN FILE | WRITE ----------------------------
excel_export.export(file_path, answer_01, answer_02, katastima)
excel_export.export(detailed_file_path, final_result, answer_02, katastima)

# -------------SEND E-MAIL----------------------------
send_mail.send_mail(mail_lst, mail_names, word, file_path, output_file)

# ----------------SLACK BOT CHAT----------------------------
slack_app.send_text(f"""
>ΔΗΜΙΟΥΡΓΙΑ ΠΡΟΣΩΡΙΝΗΣ ΕΓΓΡΑΦΗΣ 
`ΑΡΧΕΙΟ ΓΙΑ ΑΠΟΣΤΟΛΗ: {output_file}`
`ΑΡΧΕΙΟ ΜΕ ΑΝΑΛΥΤΙΚΕΣ ΠΛΗΡΟΦΟΡΙΕΣ: {detailed}`
`ΠΡΟΜΗΘΕΥΤΗΣ: {supplier}`
`ΥΠΟΚΑΤΑΣΤΗΜΑ: {katastima()}`
`PDA ID: {answer_02.ID[0]}`
`ΠΡΟΪΟΝΤΑ: {len(final_result)}`
`ΣΥΝΟΛΙΚΗ ΠΟΣΟΤΗΤΑ: {sum(final_result['Ποσότητα'])} ΤΕΜ`
`ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {round(final_result['SUM'].sum(), 2)} €`
""", slack_app.channels[6])

# ----------------SLACK BOT FILES----------------------------
slack_app.send_files(detailed, detailed_file_path, 'xlsx', slack_app.channels[6])
