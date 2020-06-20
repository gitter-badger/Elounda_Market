#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
import pandas as pd
from ΕΛΕΓΧΟΣ_ΤΕΛΕΥΤΑΙΑΣ_ΤΙΜΗΣ_ΑΓΟΡΑΣ_PDA import excel_export, scrap, sql_select
from Private import sql_connect, send_mail, slack_app

# ----------------MAKE DF REPORT VIEWABLE----------------------------
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -------------------- OPEN HTML FILE FOR THE BODY MAIL --------------------
with open('mail_body.html', 'r') as html_file:
    word = html_file.read()

# -------------------- STATEMENTS HERE --------------------
type_of_documents = ['ΑΠ_ΜΟΒ', 'ΔΕΑ', 'ΑΔΠ']
choose = type_of_documents[1]
id = 3946  # ΑΥΤΗ Η ΠΑΡΑΜΕΤΡΟΣ ΚΑΘΕ ΦΟΡΑ ΑΛΛΑΖΕΙ
output_file = 'Output.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Ανάλυση Τιμών (Κομμάς)', 'Ανάλυση Τιμών (Λογιστήριο)', 'Ανάλυση Τιμών (Κατάστημα)']

# -------------------- READ PDA SCANNED ITEMS --------------------
barcodes = pd.read_sql_query(sql_select.pda_results(id, choose), sql_connect.sql_cnx())

# -------------------- GET LATEST COST FOR EVERY BARCODE --------------------
sql_answer = pd.DataFrame()
for barcode in barcodes['BARCODE']:
    sql_answer = sql_answer.append(pd.read_sql_query(sql_select.get_product_cost(barcode), sql_connect.sql_cnx()))

# -------------------- RESET INDEX --------------------
sql_answer = sql_answer.reset_index(drop=True)
print(sql_answer)
# -------------------- FIND PRICES IN THE WEB --------------------
lista = sql_answer['BARCODE']
scrap.shops = [scrap.a, scrap.b, scrap.e]
out = scrap.calculate_prices(lista)

# -------------------- ASSIGN THE RESULTS --------------------
sql_answer['ΤΙΜΗ BAZAAR'] = out['BAZAAR']
sql_answer['TIMH ΒΑΣΙΛΟΠΟΥΛΟΣ'] = out['ΑΒ. Βασιλόπουλος']
sql_answer['TIMH Care Market'] = out['Care Market']

# -------------------- IMPORT DATA TO EXCEL --------------------
excel_export.export(path_to_file, sql_answer)

# -------------------- SEND E-MAIL --------------------
send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)

# ---------------- SLACK BOT ----------------
slack_app.send_text(f"""
>ΕΛΕΓΧΟΣ_ΤΕΛΕΥΤΑΙΑΣ_ΤΙΜΗΣ_ΑΓΟΡΑΣ_PDA: {id}
`Ενημερώθηκε Το Αρχείο: {output_file}`
""", slack_app.channels[1])


