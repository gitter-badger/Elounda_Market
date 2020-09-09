#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved

import pandas as pd
from Private import send_mail, sql_connect
from Send_Multiple_E_Mails.Libraries import pe_00_to_excel
output_file = 'Extra_Timokatalogos.xlsx'
path_to_file = f'/Users/kommas/OneDrive/Business_Folder/Slack/Multiple_emails/{output_file}'
mail_lst = ['johnkommas@hotmail.com', 'accounts@latocrete.gr', 'eloundamarket@yahoo.gr']
mail_names = ['Αλλαγή Τιμοκαταλόγου: Κομμάς', 'Αλλαγή Τιμοκαταλόγου: Λογιστήριο', 'Αλλαγή Τιμοκαταλόγου: Κατάστημα']
program_title = 'Επιπλέον Τιμοκατάλογος'

# -------------------------------- READ HTML FILE ---------------------------------------
with open('../HTML/0. Προσφορές Επιπλέον.html', 'r') as html_file:
    word = html_file.read()

# -------------------------------- READ SQL FILE ---------------------------------------
with open('../SQL/0. Προσφορές Επιπλέον', 'r') as sql_file:
    sql_querry = sql_file.read()

# --------------------------------  SQL  ---------------------------------------
sql_answer = pd.read_sql_query(sql_querry, sql_connect.sql_cnx())

# -------------------------------- EXCEL ---------------------------------------
pe_00_to_excel.run(path_to_file, sql_answer)

# -------------------------------- MAIL ---------------------------------------
send_mail.send_mail(mail_lst, mail_names, word, path_to_file, output_file)
